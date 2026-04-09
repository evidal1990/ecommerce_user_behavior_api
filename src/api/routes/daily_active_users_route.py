from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.daily_active_users_service import (
    get_daily_active_users_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "device_type",
    "age_group",
    "premium_subscription_group",
    "brand_loyalty_score_group",
}

router = APIRouter(
    prefix="/daily-active-users",
    tags=["Daily Active Users"],
)


@router.get("")
def daily_active_users_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_daily_active_users_by_dimension(dimension)
    )
