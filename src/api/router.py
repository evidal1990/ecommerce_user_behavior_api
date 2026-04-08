from fastapi import APIRouter
from src.api.routes.premium_adoption_route import router as premium_adoption_router
from src.api.routes.avg_daily_session_time_route import router as avg_daily_session_time
from src.api.routes.avg_app_usage_frequency_route import router as avg_app_usage_frequency
from src.api.routes.avg_product_views_route import router as avg_product_views
from src.api.routes.user_route import router as user_route

api_router = APIRouter()

api_router.include_router(premium_adoption_router)
api_router.include_router(avg_daily_session_time)
api_router.include_router(avg_app_usage_frequency)
api_router.include_router(avg_product_views)
api_router.include_router(user_route)
