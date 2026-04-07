from fastapi import APIRouter
from src.api.routes.premium_adoption_route import router as premium_adoption_router

api_router = APIRouter()

api_router.include_router(premium_adoption_router)
