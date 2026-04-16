from fastapi import APIRouter
from .routes import user_route

api_router = APIRouter()
api_router.include_router(user_route)
