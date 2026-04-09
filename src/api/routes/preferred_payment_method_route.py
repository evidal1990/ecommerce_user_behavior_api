from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.preferred_payment_method_service import (
    get_preferred_payment_method_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "annual_income_group",  
    "device_type",
    "cart_abandonment_rate_group",
}

router = APIRouter(
    prefix="/preferred-payment-method",
    tags=["Preferred Payment Method"],
)


@router.get("")
def preferred_payment_method_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_preferred_payment_method_by_dimension(dimension)
    )
