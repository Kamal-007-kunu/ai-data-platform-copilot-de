from fastapi import FastAPI
from app.core.config import settings
from app.api.router import api_router 
app = FastAPI(
    title = settings.app_name,
    description="Production Grade Bimbo",
    version= settings.app_version,
    environment=settings.environment
)

app.include_router(api_router)

