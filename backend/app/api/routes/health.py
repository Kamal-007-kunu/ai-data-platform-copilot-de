from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(tags=["Health"])

@router.get("/health")
async def health_check():
    return {
        "status" : "Healthy"
    }

@router.get("/ready")
async def readiness_check():
    return {
        "status" : "Ready"
    }

@router.get("/version")
async def version_check():
    return {
        "application_name" : settings.app_name,
        "application_version" : settings.app_version,
        "environment": settings.environment

    }