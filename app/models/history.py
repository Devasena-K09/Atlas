from pydantic import BaseModel

class HistoryItem(BaseModel):
    timestamp: str
    cpu_percent: float
    memory_percent: float