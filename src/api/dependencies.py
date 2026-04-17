from fastapi import Header, HTTPException

from src.core.config import settings


def get_api_key(x_api_key: str = Header(...)):
    if settings.API_KEY is None or x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return x_api_key
