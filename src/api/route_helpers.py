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
        logger.error("PostgreSQL query error: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=str(exc) if settings.DATABASE_EXPOSE_ERRORS else "Internal server error",
        ) from exc
    except (OperationalError, InterfaceError) as exc:
        if isinstance(exc, OperationalError) and "tenant or user not found" in str(
            exc
        ).lower():
            logger.error(
                "Supabase pooler: use user postgres.<project_ref> and port 5432 (Session pooler)."
            )
        logger.error("PostgreSQL connection error: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=503,
            detail=(
                str(exc)
                if settings.DATABASE_EXPOSE_ERRORS
                else "Database temporarily unavailable"
            ),
        ) from exc
    except DatabaseError as exc:
        logger.error("PostgreSQL error: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=str(exc) if settings.DATABASE_EXPOSE_ERRORS else "Internal server error",
        ) from exc
    except Psycopg2Error as exc:
        logger.error("PostgreSQL error: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=str(exc) if settings.DATABASE_EXPOSE_ERRORS else "Internal server error",
        ) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc
