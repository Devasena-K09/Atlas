from fastapi import FastAPI

from app.routes.metrics import router as metrics_router
from app.routes.system_info import router as system_router
from app.routes.health import router as health_router
from app.routes import history
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Atlas",
    description="AI-Powered Distributed Cloud Observability Platform",
    version="0.7.0"
)

app.include_router(metrics_router)
app.include_router(system_router)
app.include_router(health_router)
app.include_router(history.router)

@app.get("/")
def home():
    return {"message": "Atlas Running"}