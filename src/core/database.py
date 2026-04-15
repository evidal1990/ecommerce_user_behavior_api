import logging
import socket

import psycopg2
from src.core.config import settings

logger = logging.getLogger(__name__)


def _ipv4_for_host(hostname: str) -> str | None:
    try:
        infos = socket.getaddrinfo(hostname, None, socket.AF_INET, socket.SOCK_STREAM)
    except OSError as exc:
        logger.warning("IPv4 lookup failed for %s: %s", hostname, exc)
        return None
    if not infos:
        return None
    return infos[0][4][0]


def get_connection() -> psycopg2.extensions.connection:
    if not all(
        (
            settings.DB_POOLER_HOST,
            settings.DB_NAME,
            settings.DB_USER,
            settings.DB_PASSWORD,
        )
    ):
        raise RuntimeError(
            "Database not configured: set SUPABASE_POOLER_HOST (Session pooler hostname), "
            "SUPABASE_DB_NAME, SUPABASE_DB_USER, SUPABASE_DB_PASSWORD. "
            "Optional: SUPABASE_DB_PORT (default 5432 for Session pooler)."
        )

    kwargs = {
        "host": settings.DB_POOLER_HOST,
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
    ipv4 = _ipv4_for_host(settings.DB_POOLER_HOST)
    if ipv4:
        kwargs["hostaddr"] = ipv4
    return psycopg2.connect(**kwargs)
