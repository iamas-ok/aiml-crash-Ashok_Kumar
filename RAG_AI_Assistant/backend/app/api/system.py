from fastapi import APIRouter

from app.rag.models import SUPPORTED_MODELS, DEFAULT_MODEL

router = APIRouter(
    tags=["System"]
)


@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "message": "RAG AI Assistant API is running"
    }


@router.get("/models")
def get_models():

    return {
        "default_model": DEFAULT_MODEL,
        "models": SUPPORTED_MODELS
    }