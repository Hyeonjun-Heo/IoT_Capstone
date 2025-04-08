from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import json
from pathlib import Path

from app.database import engine, get_db
from app.models import models

# 테이블 생성 (이미 있으면 무시됨)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SmartParm 백엔드 준비 완료!"}

