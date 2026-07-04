from app.rag.model_manager import ModelManager

class TextEmbedder:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):

        self.model = ModelManager.get_embedding_model()

    def generate_embeddings(self, chunks):

        embeddings = []

        for chunk in chunks:

            vector = self.model.encode(
                chunk["chunk"],
                convert_to_numpy=True
            )

            embeddings.append(
            {
                "id": chunk["id"],
                "file_name": chunk["file_name"],
                "chunk_id": chunk["chunk_id"],
                "start_index": chunk["start_index"],
                "end_index": chunk["end_index"],
                "chunk": chunk["chunk"],
                "embedding": vector,
            }
        )

        return embeddings