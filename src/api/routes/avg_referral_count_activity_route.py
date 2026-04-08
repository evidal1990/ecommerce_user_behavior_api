from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.avg_referral_count_activity_service import (
    get_avg_referral_count_activity_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "age_group",
    "app_usage_frequency_per_week_group",
    "brand_loyalty_score_group",
    "premium_subscription_group",
    "social_sharing_frequency_per_year_group",
}

router = APIRouter(
    prefix="/avg-referral-count-activity",
    tags=["Average Referral Count Activity"],
)


@router.get("")
def avg_referral_count_activity_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_avg_referral_count_activity_by_dimension(dimension)
    )
