from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.avg_purchase_conversion_rate_service import (
    get_avg_purcaase_conversion_rate_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "app_usage_frequency_per_week_group",
    "brand_loyalty_score_group",
    "browse_to_buy_ratio_group",
    "country",
    "device_type",
    "social_sharing_frequency_per_year_group",
}

router = APIRouter(
    prefix="/avg-purchase-conversion-rate",
    tags=["Average Purchase Conversion Rate"],
)


@router.get("")
def avg_purchase_conversion_rate_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_avg_purcaase_conversion_rate_by_dimension(dimension)
    )
