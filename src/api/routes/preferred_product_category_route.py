from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.preferred_product_category_service import (
    get_preferred_product_category_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "device_type",
}

router = APIRouter(
    prefix="/preferred-product-category",
    tags=["Preferred Product Category"],
)


@router.get("")
def preferred_product_category_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(
        lambda: get_preferred_product_category_by_dimension(dimension)
    )
