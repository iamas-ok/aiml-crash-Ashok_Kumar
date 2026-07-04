from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    model_name: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    retrieved_chunks: list
    metrics: dict