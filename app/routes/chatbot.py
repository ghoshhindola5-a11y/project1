from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Response
from app.utils.compressor import get_question
from app.survey_engine import generate_followup
from app.schemas import ChatRequest, ChatResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat/{session_id}", response_model=ChatResponse)
def chat(session_id: str, request: ChatRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.session_id == session_id).first()

    if not user:
        user = User(session_id=session_id)
        db.add(user)
        db.commit()
        db.refresh(user)

    if request.answer:
        response = Response(
            user_id=user.id,
            question="Survey Question",
            answer=request.answer
        )
        db.add(response)
        db.commit()

    responses = db.query(Response).filter(Response.user_id == user.id).all()
    history = [r.answer for r in responses]

    question_index = len(responses)
    next_question = get_question(question_index)

    if not next_question:
        return ChatResponse(message="Survey Completed 🎉 Thank you!")

    enhanced_question = generate_followup(next_question, history)

    return ChatResponse(question=enhanced_question)
