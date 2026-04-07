from fastapi import APIRouter
from src.api.routes.premium_adoption_route import router as premium_adoption_router
from src.api.routes.avg_daily_session_time_route import router as avg_daily_session_time
from src.api.routes.avg_app_usage_frequency_route import router as avg_app_usage_frequency

api_router = APIRouter()

api_router.include_router(premium_adoption_router)
api_router.include_router(avg_daily_session_time)
api_router.include_router(avg_app_usage_frequency)
