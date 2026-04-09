from fastapi import APIRouter, Query
from src.api.route_helpers import execute_or_http_error
from src.services.user_service import (
    get_users_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "device_type",
    "annual_income_group",
    "education_level",
    "gender",
    "has_children",
    "employment_status",
    "urban_rural",
    "premium_subscription_group",
}

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
def users_by_dimension(dimension: str = Query(...)):
    return execute_or_http_error(lambda: get_users_by_dimension(dimension))
