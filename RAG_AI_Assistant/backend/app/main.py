from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user import User
from app.api.auth import router as auth_router
from app.api.system import router as system_router
from app.api.chat import router as chat_router
app = FastAPI(
    title="RAG AI Assistant API",
    description="Production-ready RAG AI Assistant Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(
    auth_router,
    prefix="/api/v1",
)
app.include_router(
    system_router,
    prefix="/api/v1",
)
app.include_router(
    chat_router,
    prefix="/api/v1",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to RAG AI Assistant API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }