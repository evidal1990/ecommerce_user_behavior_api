from fastapi import APIRouter
from src.api.route_helpers import execute_or_http_error
from src.services import user_service

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


@router.get("/annual-income-group")
def users_by_dimension():
    return execute_or_http_error(
        lambda: user_service.users_by_annual_income_group(),
    )


@router.get("/")
def total_users():
    return execute_or_http_error(lambda: user_service.total_users())