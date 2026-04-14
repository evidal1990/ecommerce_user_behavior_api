import logging
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import psycopg2
from src.core.config import settings

logger = logging.getLogger(__name__)


def _database_url_with_defaults(url: str) -> str:
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    parts = urlparse(url)
    qsl = parse_qsl(parts.query, keep_blank_values=True)
    keys_lower = {k.lower() for k, _ in qsl}
    extra = []
    if "sslmode" not in keys_lower:
        extra.append(("sslmode", "require"))
    if "gssencmode" not in keys_lower:
        extra.append(("gssencmode", "disable"))
    new_query = urlencode(list(qsl) + extra)
    return urlunparse(
        (
            parts.scheme,
            parts.netloc,
            parts.path,
            parts.params,
            new_query,
            parts.fragment,
        )
    )


def get_connection():
    url = settings.DATABASE_URL
    if url:
        return psycopg2.connect(_database_url_with_defaults(url))

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
    }
    if settings.DB_PORT:
        kwargs["port"] = settings.DB_PORT
    kwargs["gssencmode"] = "disable"
    return psycopg2.connect(**kwargs)
