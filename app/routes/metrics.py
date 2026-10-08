from fastapi import APIRouter
from app.services.metrics_store import get_metrics
from app.models.metrics import MetricsResponse

router = APIRouter(tags=["Metrics"])

@router.get(
    "/metrics",
    response_model=MetricsResponse
)
def metrics():
    return get_metrics()