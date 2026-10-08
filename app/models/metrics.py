from pydantic import BaseModel

class MetricsResponse(BaseModel):
    timestamp: str
    cpu_percent: float
    memory_percent: float