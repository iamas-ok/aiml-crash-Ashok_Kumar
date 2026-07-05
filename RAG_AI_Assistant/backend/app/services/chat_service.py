import json

from sqlalchemy.orm import Session

from app.models.chat_history import ChatHistory


class ChatService:

    @staticmethod
    def save_chat(
        db: Session,
        user_id: int,
        question: str,
        response: dict,
        model_name: str,
    ):

        chat = ChatHistory(
            user_id=user_id,
            question=question,
            answer=response["answer"],
            model_name=model_name,
            sources=json.dumps(response["sources"]),
        )

        db.add(chat)
        db.commit()
        db.refresh(chat)

        return chat

    @staticmethod
    def get_chat_history(
        db: Session,
        user_id: int,
    ):

        chats = (
            db.query(ChatHistory)
            .filter(ChatHistory.user_id == user_id)
            .order_by(ChatHistory.created_at.desc())
            .all()
        )

        return chats