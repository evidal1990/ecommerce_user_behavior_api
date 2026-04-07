from fastapi import APIRouter, HTTPException
from src.services.premium_adoption_service import (
    list_by_country,
    list_by_age_group,
    list_by_annual_income_group,
    list_by_education_level,
    list_by_device_type,
)

router = APIRouter(prefix="/premium-adoption", tags=["Premium Adoption"])


def _execute_or_http_error(handler):
    try:
        return handler()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc),) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc


@router.get("/by-country")
def premium_adoption_by_country():
    return _execute_or_http_error(list_by_country)


@router.get("/by-age-group")
def premium_adoption_by_age_group():
    return _execute_or_http_error(list_by_age_group)


@router.get("/by-annual-income-group")
def premium_adoption_by_annual_income():
    return _execute_or_http_error(list_by_annual_income_group)


@router.get("/by-education-level")
def premium_adoption_by_education_level():
    return _execute_or_http_error(list_by_education_level)


@router.get("/by-device-type")
def premium_adoption_by_device_type():
    return _execute_or_http_error(list_by_device_type)
