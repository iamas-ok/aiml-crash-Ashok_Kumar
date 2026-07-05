from fastapi import APIRouter, Depends, HTTPException
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


@router.post("", response_model=ChatResponse)
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


@router.get("/history")
def get_chat_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    chats = ChatService.get_chat_history(
        db=db,
        user_id=current_user.id,
    )

    return chats


@router.get("/{chat_id}")
def get_chat(
    chat_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    chat = ChatService.get_chat_by_id(
        db=db,
        chat_id=chat_id,
        user_id=current_user.id,
    )

    if chat is None:
        raise HTTPException(
            status_code=404,
            detail="Chat not found",
        )

    return chat
@router.delete("/{chat_id}")
def delete_chat(
    chat_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    deleted = ChatService.delete_chat(
        db=db,
        chat_id=chat_id,
        user_id=current_user.id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Chat not found",
        )

    return {
        "message": "Chat deleted successfully"
    }
@router.post("/{chat_id}/regenerate")
def regenerate_chat(
    chat_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    chat = ChatService.get_chat_by_id(
        db=db,
        chat_id=chat_id,
        user_id=current_user.id,
    )

    if chat is None:
        raise HTTPException(
            status_code=404,
            detail="Chat not found",
        )

    response = rag.ask(
        question=chat.question,
        model_name=chat.model_name,
    )

    ChatService.update_chat(
        db=db,
        chat=chat,
        response=response,
        model_name=chat.model_name,
    )

    return response