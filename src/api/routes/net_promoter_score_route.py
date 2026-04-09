from fastapi import APIRouter, HTTPException, Query
from src.api.route_helpers import execute_or_http_error
from src.services.net_promoter_score_service import (
    get_net_promoter_score_by_dimension,
)

ALLOWED_DIMENSIONS = {
    "country",
    "age_group",
    "browse_to_buy_ratio_group",
    "purchase_conversion_rate_group",
    "impulse_buying_score_group",
    "return_rate_group",
}

router = APIRouter(
    prefix="/net-promoter-score",
    tags=["Net Promoter Score"],
)


@router.get("")
def net_promoter_score_by_dimension(dimension: str = Query(...)):
    if dimension not in ALLOWED_DIMENSIONS:
        raise HTTPException(status_code=400, detail="Invalid dimension")
    return execute_or_http_error(lambda: get_net_promoter_score_by_dimension(dimension))
