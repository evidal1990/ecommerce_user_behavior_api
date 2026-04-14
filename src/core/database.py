import psycopg2
from src.core.config import settings


def get_connection():
    url = settings.DATABASE_URL
    if url and url.startswith("postgres://"):
        return psycopg2.connect(url.replace("postgres://", "postgresql://", 1))

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
    return psycopg2.connect(**kwargs)
