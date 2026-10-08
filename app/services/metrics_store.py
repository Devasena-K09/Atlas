from datetime import datetime
import psutil

from app.database import SessionLocal
from app.models.metric_record import MetricRecord


def get_metrics():
    db = SessionLocal()

    metric = MetricRecord(
        timestamp=datetime.now().isoformat(),
        cpu_percent=psutil.cpu_percent(interval=1),
        memory_percent=psutil.virtual_memory().percent
    )

    db.add(metric)
    db.commit()

    response = {
        "timestamp": metric.timestamp,
        "cpu_percent": metric.cpu_percent,
        "memory_percent": metric.memory_percent
    }

    db.close()

    return response