from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker


loader = DocumentLoader("synthetic_data")

documents = loader.load_documents()


chunker = TextChunker(
    chunk_size=500,
    overlap=50,
)

chunks = chunker.chunk_documents(documents)


print(f"\nTotal Chunks : {len(chunks)}\n")

for i, chunk in enumerate(chunks[:5], start=1):

    print(f"Chunk {i}")

    print("File :", chunk["file_name"])

    print("Length :", len(chunk["chunk"]))

    print(chunk["chunk"][:100])

    print("-" * 60)
    