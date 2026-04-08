from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.avg_daily_session_time_service import (
    get_avg_daily_session_time_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "device_type",
}

router = APIRouter(
    prefix="/avg-daily-session-time",
    tags=["Average Daily Session Time"],
)


@router.get("")
def avg_daily_session_time_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_avg_daily_session_time_by_dimension(dimension)
    )
