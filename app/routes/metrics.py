from fastapi import APIRouter
import psutil

router = APIRouter()


@router.get("/metrics")
def get_metrics():

    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }