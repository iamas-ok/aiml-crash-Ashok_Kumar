from sentence_transformers import SentenceTransformer


class ModelManager:

    _embedding_model = None

    @classmethod
    def get_embedding_model(cls):

        if cls._embedding_model is None:

            print("Loading embedding model...")

            cls._embedding_model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

        return cls._embedding_model