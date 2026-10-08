from fastapi import APIRouter
from app.models.health import HealthResponse
from app.services.health import get_health_status

router = APIRouter()

@router.get(
    "/health",
    tags=["Health"],
    summary="Check service health",
    description="Returns current health status of Atlas service.",
    response_model=HealthResponse
)
def health():
    return get_health_status()