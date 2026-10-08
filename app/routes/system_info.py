from fastapi import APIRouter
from app.models.system_info import SystemInfoResponse
from app.services.system_info import get_system_info

router = APIRouter()

@router.get(
    "/system-info",
    tags=["System"],
    summary="Get system information",
    description="Returns platform and processor information.",
    response_model=SystemInfoResponse
)
def system_info():
    return get_system_info()