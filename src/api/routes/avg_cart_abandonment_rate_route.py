from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.avg_cart_abandonment_rate_service import (
    get_avg_cart_abandonment_rate_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "annual_income_group",
    "preferred_payment_method",
    "stress_from_financial_decisions_level_group",
}

router = APIRouter(
    prefix="/avg-cart-abandonment-rate",
    tags=["Average Cart Abandonment Rate"],
)


@router.get("")
def avg_cart_abandonment_rate_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_avg_cart_abandonment_rate_by_dimension(dimension)
    )
