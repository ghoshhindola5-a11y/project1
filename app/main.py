from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import chatbot, analytics
from app.config import FRONTEND_URL

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Survey Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL] if FRONTEND_URL else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot.router, prefix="/api")
app.include_router(analytics.router, prefix="/api/analytics")
