class TextChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            text = document["content"]

            start = 0

            while start < len(text):

                end = start + self.chunk_size

                chunk_text = text[start:end]
                if len(chunk_text.strip()) < 50:
                 break
                

                chunk_id = len(chunks) + 1

                chunks.append(
                    {
                        "id": f"{document['file_name']}_{chunk_id}",
                        "file_name": document["file_name"],
                        "chunk_id": chunk_id,
                        "start_index": start,
                        "end_index": min(end, len(text)),
                        "chunk": chunk_text,
                    }
                )

                start += self.chunk_size - self.overlap

        return chunks