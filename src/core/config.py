import os
from pathlib import Path


def _load_local_env_file() -> None:
    env_file = Path(".env")
    if not env_file.exists():
        return

    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_local_env_file()


def _strip_env(key: str) -> str | None:
    value = os.getenv(key)
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def db_prefer_ipv4(host: str | None) -> bool:
    """
    Render often egresses over IPv6; the path to Supabase can hang or drop during SSL,
    leaving Postgres logs as 'connection received' with user/database still null.

    Default (env unset): enable for *.supabase.co hostnames.
    DB_PREFER_IPV4=false: disable. DB_PREFER_IPV4=true: force try for any host.
    """
    if not host:
        return False
    raw = os.getenv("DB_PREFER_IPV4")
    if raw is None or raw.strip() == "":
        return "supabase.co" in host.lower()
    if raw.strip().lower() in ("0", "false", "no", "off"):
        return False
    if raw.strip().lower() in ("1", "true", "yes", "on"):
        return True
    return False


class Settings:
    # Set to "1" on Render only while debugging; shows Postgres message in API responses.
    DATABASE_EXPOSE_ERRORS = os.getenv("DATABASE_EXPOSE_ERRORS", "").lower() in (
        "1",
        "true",
        "yes",
    )

    DATABASE_URL = _strip_env("DATABASE_URL")

    # Optional: Session pooler hostname from Supabase (Database → Connection pooling).
    # Direct db.<ref>.supabase.co is often IPv6-only; Render→IPv6 can fail before auth (503).
    # Example: aws-0-sa-east-1.pooler.supabase.com with SUPABASE_DB_PORT=5432 and user postgres.<ref>
    DB_POOLER_HOST = _strip_env("SUPABASE_POOLER_HOST")

    DB_HOST = _strip_env("SUPABASE_DB_HOST")
    DB_NAME = _strip_env("SUPABASE_DB_NAME")
    DB_USER = _strip_env("SUPABASE_DB_USER")
    _raw_password = os.getenv("SUPABASE_DB_PASSWORD")
    DB_PASSWORD = _raw_password.strip() if _raw_password is not None else None
    DB_PORT = _strip_env("SUPABASE_DB_PORT")
    DB_SSLMODE = (os.getenv("DB_SSLMODE") or "require").strip() or "require"
    # Only passed to libpq if set (e.g. "disable"); avoids invalid-option errors on older clients.
    DB_GSSENCMODE = _strip_env("DB_GSSENCMODE")


settings = Settings()
