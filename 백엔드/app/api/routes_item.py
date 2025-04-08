import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from pathlib import Path

from app.database import get_db
from app.models.sensor_data import SensorData

router = APIRouter()

@router.post("/insert-dummy-data")
def insert_dummy_data(db: Session = Depends(get_db)):
    path = Path("data/dummy_sensor_data.json")
    with open(path, "r", encoding="utf-8") as f:
        sensor_list = json.load(f)

    for item in sensor_list:
        sensor = SensorData(
            timestamp=datetime.fromisoformat(item["timestamp"]),
            temperature=item["temperature"],
            humidity=item["humidity"],
            soil_moisture=item["soil_moisture"],
            light=item["light"],
            image_path=item["image_path"]
        )
        db.add(sensor)

    db.commit()
    return {"message": f"{len(sensor_list)} rows inserted!"}
