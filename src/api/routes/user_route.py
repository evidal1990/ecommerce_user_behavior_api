from fastapi import APIRouter, Query
from src.api.route_helpers import execute_or_http_error
from src.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def users_root(
    group_by: str | None = Query(
        None,
        description="Ex.: country, gender, age_group",
    )
):
    if group_by is not None:
        return execute_or_http_error(
            lambda: user_service.users_by_dimension(group_by),
        )
    return execute_or_http_error(lambda: user_service.total_users())
