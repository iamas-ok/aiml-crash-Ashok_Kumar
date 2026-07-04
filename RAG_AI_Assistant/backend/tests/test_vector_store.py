from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.embedder import TextEmbedder
from app.rag.vector_store import ChromaVectorStore


loader = DocumentLoader("synthetic_data")
documents = loader.load_documents()

chunker = TextChunker(
    chunk_size=500,
    overlap=50,
)

chunks = chunker.chunk_documents(documents)

embedder = TextEmbedder()

embeddings = embedder.generate_embeddings(chunks)

vector_store = ChromaVectorStore()

vector_store.add_embeddings(embeddings)

print(f"\nStored {len(embeddings)} embeddings in ChromaDB")