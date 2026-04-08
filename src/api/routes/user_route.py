from fastapi import APIRouter, HTTPException
from src.services.user_service import (
    list_by_employment_status,
    list_by_annual_income_group,
    list_by_age_group,
    list_by_device_type,
    list_by_neighborhood,
    list_by_education_level,
    list_by_gender,
    list_by_country,
    list_by_has_children,
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


@router.get("/by-age-group")
def users_by_age_group():
    return _execute_or_http_error(list_by_age_group)


@router.get("/by-device-type")
def users_by_device_type():
    return _execute_or_http_error(list_by_device_type)


@router.get("/by-neighborhood")
def users_by_neighborhood():
    return _execute_or_http_error(list_by_neighborhood)


@router.get("/by-education-level")
def users_by_education_level():
    return _execute_or_http_error(list_by_education_level)


@router.get("/by-gender")
def users_by_gender():
    return _execute_or_http_error(list_by_gender)


@router.get("/by-country")
def users_by_country():
    return _execute_or_http_error(list_by_country)


@router.get("/by-has-children")
def users_by_country():
    return _execute_or_http_error(list_by_has_children)
