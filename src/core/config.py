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


class Settings:
    DB_HOST = os.getenv("SUPABASE_DB_HOST")
    DB_NAME = os.getenv("SUPABASE_DB_NAME")
    DB_USER = os.getenv("SUPABASE_DB_USER")
    DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
    DB_PORT = os.getenv("SUPABASE_DB_PORT")


settings = Settings()
