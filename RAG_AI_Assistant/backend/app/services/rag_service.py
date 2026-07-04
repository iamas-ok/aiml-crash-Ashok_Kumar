import time

from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.rag.llm import LLMClient
from app.services.response_formatter import ResponseFormatter


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

        # Start timer
        start = time.perf_counter()

        # Retrieve relevant chunks
        chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k,
        )

        # Build prompt
        prompt = PromptBuilder.build_prompt(
            query=question,
            retrieved_chunks=chunks,
        )

        # Generate LLM response
        answer = self.llm.generate_response(
            prompt=prompt,
            model_name=model_name,
        )

        # Calculate response time
        response_time = time.perf_counter() - start

        # Return formatted response
        return ResponseFormatter.format_response(
            answer=answer,
            chunks=chunks,
            model=model_name,
            response_time=response_time,
            top_k=top_k,
        )