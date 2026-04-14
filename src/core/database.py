import logging
import re
import socket
from urllib.parse import urlparse

import psycopg2
from src.core.config import db_prefer_ipv4, settings

logger = logging.getLogger(__name__)
_logged_supabase_ipv6_only = False
_logged_database_url_direct = False


def _database_url_with_sslmode(url: str) -> str:
    """Append sslmode only if missing; avoid re-parsing query (breaks Supabase options=...)."""
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    if "sslmode=" not in url.lower():
        sep = "&" if "?" in url else "?"
        url = f"{url}{sep}sslmode=require"
    return url


def _first_ipv4(host: str) -> str | None:
    try:
        infos = socket.getaddrinfo(host, None, socket.AF_INET, socket.SOCK_STREAM)
    except OSError as exc:
        logger.warning("Could not resolve IPv4 for %s: %s", host, exc)
        return None
    if not infos:
        return None
    return infos[0][4][0]


def _is_supabase_direct_db_host(host: str) -> bool:
    h = host.lower().rstrip(".")
    return h.startswith("db.") and h.endswith(".supabase.co")


def _log_ipv6_only_supabase(host: str) -> None:
    global _logged_supabase_ipv6_only
    if not _is_supabase_direct_db_host(host):
        return
    if _first_ipv4(host) is not None:
        return
    if _logged_supabase_ipv6_only:
        return
    _logged_supabase_ipv6_only = True
    m = re.match(r"^db\.([^.]+)\.supabase\.co\.?$", host, re.IGNORECASE)
    pooler_user = f"postgres.{m.group(1)}" if m else "postgres.<project_ref>"
    logger.error(
        "Host %s has no IPv4 (A record); only IPv6. Traffic from many hosts (e.g. Render) "
        "often fails before PostgreSQL authentication. Set env SUPABASE_POOLER_HOST to the "
        "Session pooler hostname from Supabase → Database → Connection pooling "
        "(e.g. aws-0-sa-east-1.pooler.supabase.com), SUPABASE_DB_PORT=5432, and "
        "SUPABASE_DB_USER=%s (keep password and database name as in the pooler URI).",
        host,
        pooler_user,
    )


def _database_url_ready(url: str) -> str:
    url = _database_url_with_sslmode(url)
    hostname = urlparse(url).hostname
    if not hostname or not db_prefer_ipv4(hostname):
        return url
    if "hostaddr=" in url.lower():
        return url
    ipv4 = _first_ipv4(hostname)
    if not ipv4:
        return url
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}hostaddr={ipv4}"


def _warn_if_database_url_uses_direct_supabase(url: str) -> None:
    global _logged_database_url_direct
    if _logged_database_url_direct:
        return
    hostname = urlparse(url).hostname or ""
    if not _is_supabase_direct_db_host(hostname):
        return
    _logged_database_url_direct = True
    logger.error(
        "DATABASE_URL points to direct host %s (often IPv6-only; Render may get intermittent 503). "
        "Prefer Session pooler: set SUPABASE_POOLER_HOST + SUPABASE_DB_* and remove DATABASE_URL on Render, "
        "or replace DATABASE_URL with the pooler URI from Supabase (port 5432, user postgres.<ref>).",
        hostname,
    )


def _connect_discrete(connect_host: str) -> psycopg2.extensions.connection:
    _log_ipv6_only_supabase(connect_host)
    kwargs = {
        "host": connect_host,
        "database": settings.DB_NAME,
        "user": settings.DB_USER,
        "password": settings.DB_PASSWORD,
        "sslmode": settings.DB_SSLMODE,
        "connect_timeout": 15,
    }
    if settings.DB_PORT:
        kwargs["port"] = settings.DB_PORT
    if settings.DB_GSSENCMODE:
        kwargs["gssencmode"] = settings.DB_GSSENCMODE
    if db_prefer_ipv4(connect_host):
        ipv4 = _first_ipv4(connect_host)
        if ipv4:
            kwargs["hostaddr"] = ipv4
    return psycopg2.connect(**kwargs)


def get_connection():
    discrete_creds = all(
        (
            settings.DB_NAME,
            settings.DB_USER,
            settings.DB_PASSWORD,
        )
    )

    # Pooler + discrete creds must win over DATABASE_URL (Render often sets a stale direct Supabase URL).
    if settings.DB_POOLER_HOST:
        if not discrete_creds:
            raise RuntimeError(
                "SUPABASE_POOLER_HOST is set but SUPABASE_DB_NAME, SUPABASE_DB_USER, and/or "
                "SUPABASE_DB_PASSWORD are missing. Fill those from the Session pooler connection string, "
                "or remove SUPABASE_POOLER_HOST."
            )
        if settings.DATABASE_URL:
            logger.warning(
                "SUPABASE_POOLER_HOST is set: connecting via pooler and ignoring DATABASE_URL."
            )
        return _connect_discrete(settings.DB_POOLER_HOST)

    url = settings.DATABASE_URL
    if url:
        _warn_if_database_url_uses_direct_supabase(url)
        return psycopg2.connect(_database_url_ready(url), connect_timeout=15)

    if not all(
        (
            settings.DB_HOST,
            settings.DB_NAME,
            settings.DB_USER,
            settings.DB_PASSWORD,
        )
    ):
        raise RuntimeError(
            "Database not configured: set DATABASE_URL or "
            "SUPABASE_DB_HOST, SUPABASE_DB_NAME, SUPABASE_DB_USER, and SUPABASE_DB_PASSWORD "
            "(for Render + Supabase, prefer SUPABASE_POOLER_HOST + those vars and omit DATABASE_URL)."
        )

    return _connect_discrete(settings.DB_HOST)
