from app.database import SessionLocal
from app.models.metric_record import MetricRecord

def get_history():
    db = SessionLocal()

    records = (
        db.query(MetricRecord)
        .order_by(MetricRecord.id.desc())
        .limit(20)
        .all()
    )

    result = []

    for record in records:
        result.append({
            "timestamp": record.timestamp,
            "cpu_percent": record.cpu_percent,
            "memory_percent": record.memory_percent
        })

    db.close()

    return result