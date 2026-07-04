from app.rag.llm import LLMClient


llm = LLMClient()

prompt = """
Say only one word.

Hello
"""

response = llm.generate_response(
    prompt=prompt,
    model_name="openai/gpt-oss-20b",
)

print("\nModel Response:\n")

print(response)