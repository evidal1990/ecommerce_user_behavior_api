from fastapi import APIRouter, HTTPException
from src.services.user_service import (
    list_by_employment_status,
    list_by_annual_income_group
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


def _execute_or_http_error(handler):
    try:
        return handler()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc


@router.get("/by-employment-status")
def users_by_employment_status():
    return _execute_or_http_error(list_by_employment_status)

@router.get("/by-annual-income")
def users_by_annual_income_group():
    return _execute_or_http_error(list_by_annual_income_group)
