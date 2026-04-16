from fastapi import APIRouter, Query

from src.api.route_helpers import execute_or_http_error
from src.services import metrics_service

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("")
def metrics_root(
    metric: str = Query(
        "total_users",
        description="Ex.: total_users, avg_coupon_usage_per_user",
    ),
):
    return execute_or_http_error(
        lambda: metrics_service.metrics_analytics(metric=metric),
    )
