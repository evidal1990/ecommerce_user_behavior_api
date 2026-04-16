from fastapi import (
    APIRouter,
    Query,
)
from src.api.route_helpers import execute_or_http_error
from src.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


from fastapi import APIRouter, Query
from src.api.route_helpers import execute_or_http_error
from src.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
def users_root(
    group_by: str | None = Query(
        None,
        description="Ex.: country, gender, education_level",
    ),
    metric: str = Query(
        "total_users",
        description="Ex.: total_users, avg_coupon_usage_per_user",
    ),
):
    return execute_or_http_error(lambda: user_service.users_analytics(group_by, metric))
