from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.avg_brand_loyalty_score_service import (
    get_avg_brand_loyalty_score_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "age_group",
    "annual_income_group",
    "country",
    "premium_subscription_group",
}

router = APIRouter(
    prefix="/avg-brand-loyalty-score",
    tags=["Average Brand Loyalty Score"],
)


@router.get("")
def avg_brand_loyalty_score_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_avg_brand_loyalty_score_by_dimension(dimension)
    )
