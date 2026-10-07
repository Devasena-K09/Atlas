from fastapi import APIRouter
import platform

router = APIRouter()

@router.get("/system-info")
def system_info():

    return {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }