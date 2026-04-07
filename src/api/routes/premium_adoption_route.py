from fastapi import APIRouter, HTTPException
from src.services.premium_adoption_service import list_by_country

router = APIRouter(prefix="/premium-adoption", tags=["Premium Adoption"])


@router.get("/by-country")
def premium_adoption_by_country():
    try:
        return list_by_country()
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        ) from exc
