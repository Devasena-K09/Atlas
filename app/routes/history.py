from fastapi import APIRouter

router = APIRouter()

sample_history = [
    {"time": "10:00", "cpu": 15},
    {"time": "10:01", "cpu": 22},
    {"time": "10:02", "cpu": 18},
    {"time": "10:03", "cpu": 35},
]

@router.get("/history")
def get_history():
    return sample_history