from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.embedder import TextEmbedder


loader = DocumentLoader("synthetic_data")
documents = loader.load_documents()

chunker = TextChunker(
    chunk_size=500,
    overlap=50,
)

chunks = chunker.chunk_documents(documents)

embedder = TextEmbedder()

embeddings = embedder.generate_embeddings(chunks)

print(f"\nTotal Embeddings : {len(embeddings)}\n")

print("File :", embeddings[0]["file_name"])

print("Chunk Length :", len(embeddings[0]["chunk"]))

print("Embedding Dimension :", len(embeddings[0]["embedding"]))

print("\nFirst 10 Values:\n")

print(embeddings[0]["embedding"][:10])