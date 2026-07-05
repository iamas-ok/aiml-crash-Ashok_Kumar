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

    @staticmethod
    def get_chat_by_id(
        db: Session,
        chat_id: int,
        user_id: int,
    ):

        chat = (
            db.query(ChatHistory)
            .filter(
                ChatHistory.id == chat_id,
                ChatHistory.user_id == user_id,
            )
            .first()
        )

        return chat

    @staticmethod
    def delete_chat(
        db: Session,
        chat_id: int,
        user_id: int,
    ):

        chat = (
            db.query(ChatHistory)
            .filter(
                ChatHistory.id == chat_id,
                ChatHistory.user_id == user_id,
            )
            .first()
        )

        if chat is None:
            return False

        db.delete(chat)
        db.commit()

        return True
    @staticmethod
    def update_chat(
        db: Session,
        chat: ChatHistory,
        response: dict,
        model_name: str,
    ):

        chat.answer = response["answer"]
        chat.model_name = model_name
        chat.sources = json.dumps(response["sources"])

        db.commit()
        db.refresh(chat)

        return chat