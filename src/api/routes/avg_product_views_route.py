from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.avg_produtct_views_service import (
    get_avg_product_views_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "device_type",
}

router = APIRouter(
    prefix="/avg-product-views",
    tags=["Average Product Views"],
)


@router.get("")
def avg_product_views_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_avg_product_views_by_dimension(dimension)
    )
