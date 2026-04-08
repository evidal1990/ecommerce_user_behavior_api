from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.avg_coupon_usage_frequency_service import (
    get_avg_coupon_usage_frequency_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "annual_income_group",
    "brand_loyalty_score_group",
    "preferred_payment_method",
}

router = APIRouter(
    prefix="/avg-coupon-usage-frequency",
    tags=["Average Coupon Usage Frequency"],
)


@router.get("")
def avg_coupon_usage_frequency_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_avg_coupon_usage_frequency_by_dimension(dimension)
    )
