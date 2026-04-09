from fastapi import APIRouter
from .routes import (
    premium_adoption_router,
    avg_daily_session_time,
    avg_app_usage_frequency,
    avg_product_views,
    avg_coupon_usage_frequency_route,
    avg_purchase_conversion_rate_route,
    user_route,
    avg_cart_abandonment_rate_route,
    avg_brand_loyalty_score_route,
    avg_referral_count_activity_route,
    churn_rate_route,
)

api_router = APIRouter()
api_router.include_router(avg_daily_session_time)
api_router.include_router(avg_app_usage_frequency)
api_router.include_router(avg_product_views)
api_router.include_router(avg_coupon_usage_frequency_route)
api_router.include_router(avg_purchase_conversion_rate_route)
api_router.include_router(avg_cart_abandonment_rate_route)
api_router.include_router(avg_brand_loyalty_score_route)
api_router.include_router(avg_referral_count_activity_route)
api_router.include_router(premium_adoption_router)
api_router.include_router(user_route)
api_router.include_router(churn_rate_route)