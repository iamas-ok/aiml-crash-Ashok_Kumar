from app.rag.loader import DocumentLoader


loader = DocumentLoader(
    "synthetic_data"
)

documents = loader.load_documents()

print(f"Loaded {len(documents)} documents\n")

for doc in documents:

    print(doc["file_name"])

    print(doc["content"][:100])

    print("-" * 50)