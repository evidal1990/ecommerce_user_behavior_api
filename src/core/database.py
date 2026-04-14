import logging
import socket
from urllib.parse import urlparse

import psycopg2
from src.core.config import db_prefer_ipv4, settings

logger = logging.getLogger(__name__)


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


def get_connection():
    url = settings.DATABASE_URL
    if url:
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
            "SUPABASE_DB_HOST, SUPABASE_DB_NAME, SUPABASE_DB_USER, and SUPABASE_DB_PASSWORD"
        )

    kwargs = {
        "host": settings.DB_HOST,
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
    if db_prefer_ipv4(settings.DB_HOST):
        ipv4 = _first_ipv4(settings.DB_HOST)
        if ipv4:
            kwargs["hostaddr"] = ipv4
    return psycopg2.connect(**kwargs)
