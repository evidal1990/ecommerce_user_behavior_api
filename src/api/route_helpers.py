import logging
from collections.abc import Callable
from typing import TypeVar

from fastapi import HTTPException
from psycopg2 import Error as Psycopg2Error
from psycopg2 import DatabaseError, InterfaceError, OperationalError, ProgrammingError

from src.core.config import settings

logger = logging.getLogger(__name__)

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
    except ProgrammingError as exc:
        logger.error("PostgreSQL query/schema error: %s", exc, exc_info=True)
        detail = (
            str(exc) if settings.DATABASE_EXPOSE_ERRORS else "Internal server error"
        )
        raise HTTPException(status_code=500, detail=detail) from exc
    except (OperationalError, InterfaceError) as exc:
        logger.error("PostgreSQL connection error: %s", exc, exc_info=True)
        detail = (
            str(exc)
            if settings.DATABASE_EXPOSE_ERRORS
            else "Database temporarily unavailable"
        )
        raise HTTPException(status_code=503, detail=detail) from exc
    except DatabaseError as exc:
        # e.g. InternalError (pooler), NotSupportedError — connection exists; not a "service down" case
        logger.error("PostgreSQL server error: %s", exc, exc_info=True)
        detail = (
            str(exc) if settings.DATABASE_EXPOSE_ERRORS else "Internal server error"
        )
        raise HTTPException(status_code=500, detail=detail) from exc
    except Psycopg2Error as exc:
        logger.error("PostgreSQL error: %s: %s", type(exc).__name__, exc, exc_info=True)
        detail = (
            str(exc) if settings.DATABASE_EXPOSE_ERRORS else "Internal server error"
        )
        raise HTTPException(status_code=500, detail=detail) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc
