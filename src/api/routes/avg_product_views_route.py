from fastapi import APIRouter, HTTPException
from src.services.avg_produtct_views_service import (
    list_by_country,
    list_by_age_group,
    list_by_device_type,
)

router = APIRouter(
    prefix="/avg-product-views",
    tags=["Average Product Views"],
)


def _execute_or_http_error(handler):
    try:
        return handler()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Internal server error") from exc


@router.get("/by-country")
def avg_product_views_by_country():
    return _execute_or_http_error(list_by_country)


@router.get("/by-age-group")
def avg_product_views_by_age_group():
    return _execute_or_http_error(list_by_age_group)


@router.get("/by-device-type")
def avg_product_views_by_device_type():
    return _execute_or_http_error(list_by_device_type)
