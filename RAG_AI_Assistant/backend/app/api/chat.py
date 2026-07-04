from fastapi import APIRouter, Depends

from app.auth.jwt_handler import get_current_user
from app.models.user import User
from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

rag = RAGService()


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
):

    response = rag.ask(
        question=request.question,
        model_name=request.model_name,
    )

    return response