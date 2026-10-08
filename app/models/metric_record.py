from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class MetricRecord(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    cpu_percent = Column(Float)
    memory_percent = Column(Float)