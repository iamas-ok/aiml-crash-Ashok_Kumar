from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.rag.llm import LLMClient


class RAGService:

    def __init__(self):

        self.retriever = Retriever()
        self.llm = LLMClient()

    def ask(
        self,
        question: str,
        model_name: str,
        top_k: int = 3,
    ):

        chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k,
        )

        prompt = PromptBuilder.build_prompt(
            query=question,
            retrieved_chunks=chunks,
        )

        answer = self.llm.generate_response(
            prompt=prompt,
            model_name=model_name,
        )

        return {
            "answer": answer,
            "chunks": chunks,
        }