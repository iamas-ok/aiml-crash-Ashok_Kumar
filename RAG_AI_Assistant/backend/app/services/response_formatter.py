import time


class ResponseFormatter:

    @staticmethod
    def format_response(
        answer: str,
        chunks: list,
        model: str,
        response_time: float,
        top_k: int,
    ):

        sources = sorted(
            list(
                {
                    chunk["file_name"]
                    for chunk in chunks
                }
            )
        )

        retrieved_chunks = []

        for chunk in chunks:

            distance = chunk["distance"]

            similarity = max(
                0,
                round((1 - distance / 2) * 100, 2)
            )

            if similarity >= 85:
                confidence = "High"
            elif similarity >= 70:
                confidence = "Medium"
            else:
                confidence = "Low"

            retrieved_chunks.append(
                {
                    "file_name": chunk["file_name"],
                    "chunk_id": chunk["chunk_id"],
                    "preview": chunk["chunk"][:200],
                    "similarity_score": similarity,
                    "confidence": confidence,
                }
            )

        return {
            "answer": answer,
            "sources": sources,
            "retrieved_chunks": retrieved_chunks,
            "metrics": {
                "model": model,
                "top_k": top_k,
                "response_time": round(response_time, 2),
            },
        }