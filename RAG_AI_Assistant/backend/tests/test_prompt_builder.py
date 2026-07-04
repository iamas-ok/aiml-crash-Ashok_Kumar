from app.rag.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder


retriever = Retriever()

query = "What are the dietary standards for patients?"

chunks = retriever.retrieve(
    query=query,
    top_k=3,
)

prompt = PromptBuilder.build_prompt(
    query=query,
    retrieved_chunks=chunks,
)

print(prompt)