from fastapi import APIRouter, Query
from src.api.route_helpers import execute_or_http_error
from src.services.premium_adoption_service import (
    get_premium_adoption_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "device_type",
    "annual_income_group",
    "education_level",
}

router = APIRouter(
    prefix="/premium-adoption",
    tags=[
        "Premium Adoption",
    ],
)


@router.get("")
def get_avg_daily_session_time_by_dimension(dimension: str = Query(...)):
    return execute_or_http_error(lambda: get_premium_adoption_by_dimension(dimension))
