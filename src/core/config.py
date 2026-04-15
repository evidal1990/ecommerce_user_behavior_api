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


class Settings:
    DATABASE_EXPOSE_ERRORS = os.getenv("DATABASE_EXPOSE_ERRORS", "").lower() in (
        "1",
        "true",
        "yes",
    )

    # Session pooler host (Supabase Connect → Session pooler). SUPABASE_DB_HOST accepted as alias.
    DB_POOLER_HOST = _strip_env("SUPABASE_POOLER_HOST") or _strip_env("SUPABASE_DB_HOST")
    DB_NAME = _strip_env("SUPABASE_DB_NAME")
    DB_USER = _strip_env("SUPABASE_DB_USER")
    _raw_password = os.getenv("SUPABASE_DB_PASSWORD")
    DB_PASSWORD = _raw_password.strip() if _raw_password is not None else None
    DB_PORT = _strip_env("SUPABASE_DB_PORT")
    DB_SSLMODE = (os.getenv("DB_SSLMODE") or "require").strip() or "require"
    DB_GSSENCMODE = _strip_env("DB_GSSENCMODE")


settings = Settings()
