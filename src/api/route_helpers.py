from collections.abc import Callable
from typing import TypeVar

from fastapi import HTTPException

T = TypeVar("T")


def execute_or_http_error(handler: Callable[[], T]) -> T:
    try:
        return handler()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc
