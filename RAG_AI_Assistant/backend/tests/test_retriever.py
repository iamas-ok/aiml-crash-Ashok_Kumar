from app.rag.retriever import Retriever


retriever = Retriever()

query = "What are the dietary standards for patients?"

results = retriever.retrieve(
    query=query,
    top_k=3,
)

print("\nRetrieved Chunks\n")

for i, item in enumerate(results, start=1):

    print("=" * 60)

    print(f"Result {i}")

    print("File :", item["file_name"])

    print("Chunk ID :", item["chunk_id"])

    print("Distance :", item["distance"])

    print()

    print(item["chunk"][:300])

    print()