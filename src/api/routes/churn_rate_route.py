from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.churn_rate_service import (
    get_churn_rate_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "device_type",
    "return_rate_group",
}

router = APIRouter(
    prefix="/churn-rate",
    tags=["Churn Rate"],
)


@router.get("")
def churn_rate_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(lambda: get_churn_rate_by_dimension(dimension))
