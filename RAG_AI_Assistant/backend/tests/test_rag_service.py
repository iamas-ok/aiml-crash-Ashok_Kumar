from app.services.rag_service import RAGService

rag = RAGService()

response = rag.ask(
    question="What are the dietary standards for patients?",
    model_name="openai/gpt-oss-20b",
    top_k=3,
)

print("\nANSWER\n")
print(response["answer"])

print("\nSOURCES\n")

for chunk in response["chunks"]:
    print("-", chunk["file_name"])
    