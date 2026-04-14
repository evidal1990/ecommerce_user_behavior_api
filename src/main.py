from fastapi import FastAPI
from src.api.router import api_router

app = FastAPI(title="Ecommerce User Behavior API")


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Ecommerce User Behavior API",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


app.include_router(api_router)
