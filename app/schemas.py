from pydantic import BaseModel
from typing import Optional, List


# -----------------------
# Chat Schemas
# -----------------------

class ChatRequest(BaseModel):
    answer: Optional[str] = None


class ChatResponse(BaseModel):
    question: Optional[str] = None
    message: Optional[str] = None


# -----------------------
# Analytics Schemas
# -----------------------

class OverviewResponse(BaseModel):
    total_users: int
    total_responses: int
    completed_surveys: int
    completion_rate_percent: float


class QuestionStats(BaseModel):
    question: str
    total_answers: int


class KeywordStat(BaseModel):
    word: str
    count: int
