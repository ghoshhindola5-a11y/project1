from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from collections import Counter
import re

from app.database import SessionLocal
from app.models import User, Response
from app.utils.compressor import total_questions
from app.schemas import OverviewResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/overview", response_model=OverviewResponse)
def overview(db: Session = Depends(get_db)):

    total_users = db.query(User).count()
    total_responses = db.query(Response).count()

    completed = (
        db.query(User)
        .join(Response)
        .group_by(User.id)
        .having(func.count(Response.id) >= total_questions())
        .count()
    )

    completion_rate = (completed / total_users * 100) if total_users > 0 else 0

    return OverviewResponse(
        total_users=total_users,
        total_responses=total_responses,
        completed_surveys=completed,
        completion_rate_percent=round(completion_rate, 2)
    )
