from fastapi import APIRouter
from src.api.route_helpers import execute_or_http_error
from src.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/premium-subscription-group")
def users_by_premium_subscription_group():
    return execute_or_http_error(
        lambda: user_service.users_by_premium_subscription_group(),
    )


@router.get("/education-level")
def users_by_education_level():
    return execute_or_http_error(
        lambda: user_service.users_by_education_level(),
    )


@router.get("/gender")
def users_by_gender():
    return execute_or_http_error(
        lambda: user_service.users_by_gender(),
    )


@router.get("/neighborhood")
def users_by_neighborhood():
    return execute_or_http_error(
        lambda: user_service.users_by_neighborhood(),
    )


@router.get("/device-type")
def users_by_device_type():
    return execute_or_http_error(
        lambda: user_service.users_by_device_type(),
    )


@router.get("/age-group")
def users_by_age_group():
    return execute_or_http_error(
        lambda: user_service.users_by_age_group(),
    )


@router.get("/annual-income-group")
def users_by_dimension():
    return execute_or_http_error(
        lambda: user_service.users_by_annual_income_group(),
    )


@router.get("/")
def total_users():
    return execute_or_http_error(lambda: user_service.total_users())
