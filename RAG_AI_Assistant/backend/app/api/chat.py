from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.jwt_handler import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService
from app.services.chat_service import ChatService

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
    db: Session = Depends(get_db),
):

    response = rag.ask(
        question=request.question,
        model_name=request.model_name,
    )

    ChatService.save_chat(
        db=db,
        user_id=current_user.id,
        question=request.question,
        response=response,
        model_name=request.model_name,
    )

    return response