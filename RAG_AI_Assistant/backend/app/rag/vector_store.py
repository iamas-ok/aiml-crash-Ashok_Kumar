import chromadb


class ChromaVectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="rag_documents"
        )

    def add_embeddings(self, embeddings):

        for item in embeddings:

            self.collection.add(
                ids=[item["id"]],

                embeddings=[
                    item["embedding"].tolist()
                ],

                documents=[
                    item["chunk"]
                ],

                metadatas=[
                    {
                        "file_name": item["file_name"],
                        "chunk_id": item["chunk_id"],
                        "start_index": item["start_index"],
                        "end_index": item["end_index"],
                    }
                ],
            )