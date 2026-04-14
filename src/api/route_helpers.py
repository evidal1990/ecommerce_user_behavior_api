from collections.abc import Callable
from typing import TypeVar

from fastapi import HTTPException
from psycopg2 import Error as Psycopg2Error

T = TypeVar("T")


def execute_or_http_error(handler: Callable[[], T]) -> T:
    try:
        return handler()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except HTTPException:
        raise
    except RuntimeError as exc:
        msg = str(exc)
        if msg.startswith("Database not configured"):
            raise HTTPException(status_code=503, detail=msg) from exc
        raise HTTPException(status_code=500, detail="Internal server error") from exc
    except Psycopg2Error as exc:
        raise HTTPException(
            status_code=503,
            detail="Database temporarily unavailable",
        ) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc
