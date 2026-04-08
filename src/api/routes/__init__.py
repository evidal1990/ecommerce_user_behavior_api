from .premium_adoption_route import router as premium_adoption_router
from .avg_daily_session_time_route import router as avg_daily_session_time
from .avg_app_usage_frequency_route import (
    router as avg_app_usage_frequency,
)
from .avg_product_views_route import router as avg_product_views
from .avg_coupon_usage_frequency_route import (
    router as avg_coupon_usage_frequency_route,
)
from .avg_purchase_conversion_rate_route import (
    router as avg_purchase_conversion_rate_route,
)
from .user_route import router as user_route
from .avg_cart_abandonment_rate_route import router as avg_cart_abandonment_rate_route

__all__ = [
    premium_adoption_router,
    avg_daily_session_time,
    avg_app_usage_frequency,
    avg_product_views,
    avg_coupon_usage_frequency_route,
    avg_purchase_conversion_rate_route,
    user_route,
    avg_cart_abandonment_rate_route,
]
