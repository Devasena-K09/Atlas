from fastapi import FastAPI

from app.metrics import router as metrics_router
from app.system_info import router as system_router
from app.health import router as health_router

app = FastAPI()

app.include_router(metrics_router)
app.include_router(system_router)
app.include_router(health_router)

@app.get("/")
def home():
    return {"message": "Atlas Running"}