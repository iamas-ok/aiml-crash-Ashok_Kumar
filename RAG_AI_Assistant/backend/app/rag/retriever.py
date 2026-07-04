from sentence_transformers import SentenceTransformer

from app.rag.vector_store import ChromaVectorStore


class Retriever:

    def __init__(self):

        self.embedder = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.vector_store = ChromaVectorStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ):

        query_embedding = self.embedder.encode(
            query,
            convert_to_numpy=True,
        )

        results = self.vector_store.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k,
        )

        retrieved_chunks = []

        for i in range(
            len(results["documents"][0])
        ):

            metadata = results["metadatas"][0][i]

            retrieved_chunks.append(
                {
                    "file_name": metadata["file_name"],
                    "chunk_id": metadata["chunk_id"],
                    "start_index": metadata["start_index"],
                    "end_index": metadata["end_index"],
                    "chunk": results["documents"][0][i],
                    "distance": results["distances"][0][i],
                }
            )

        return retrieved_chunks