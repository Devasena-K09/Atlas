from fastapi import APIRouter
from typing import List

from app.models.history import HistoryItem
from app.services.history import get_history

router = APIRouter(tags=["History"])

@router.get(
    "/history",
    response_model=List[HistoryItem]
)
def history():
    return get_history()