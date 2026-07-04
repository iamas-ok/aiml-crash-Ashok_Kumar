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
                

                chunks.append(
                    {
                        "file_name": document["file_name"],
                        "chunk": chunk_text,
                    }
                )

                start += self.chunk_size - self.overlap

        return chunks