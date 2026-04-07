from fastapi import APIRouter, HTTPException
from src.services.premium_adoption_service import (
    list_by_country,
    list_by_age_group,
    list_by_annual_income_group,
    list_by_education_level,
    list_by_device_type,
)

router = APIRouter(prefix="/premium-adoption", tags=["Premium Adoption"])


@router.get("/by-country")
def premium_adoption_by_country():
    try:
        return list_by_country()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc


@router.get("/by-age-group")
def premium_adoption_by_age_group():
    try:
        return list_by_age_group()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc


@router.get("/by-annual-income-group")
def premium_adoption_by_annual_income():
    try:
        return list_by_annual_income_group()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/by-education-level")
def premium_adoption_by_education_level():
    try:
        return list_by_education_level()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc

@router.get("/by-device-type")
def premium_adoption_by_device_type():
    try:
        return list_by_device_type()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc
