from sentence_transformers import SentenceTransformer


class TextEmbedder:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):

        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, chunks):

        embeddings = []

        for chunk in chunks:

            vector = self.model.encode(
                chunk["chunk"],
                convert_to_numpy=True
            )

            embeddings.append(
                {
                    "file_name": chunk["file_name"],
                    "chunk": chunk["chunk"],
                    "embedding": vector,
                }
            )

        return embeddings