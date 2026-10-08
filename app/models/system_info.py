from pydantic import BaseModel

class SystemInfoResponse(BaseModel):
    platform: str
    processor: str