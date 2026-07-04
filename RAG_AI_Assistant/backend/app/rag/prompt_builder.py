class PromptBuilder:

    @staticmethod
    def build_prompt(
        query: str,
        retrieved_chunks: list,
    ):

        context = ""

        for index, chunk in enumerate(retrieved_chunks, start=1):

            context += (
                f"\n"
                f"Source {index}: {chunk['file_name']}\n"
                f"{chunk['chunk']}\n"
            )

        prompt = f"""
You are an AI assistant for question answering.

Rules:
1. Answer ONLY using the provided context.
2. Do not use external knowledge.
3. If the answer is not present in the context, reply:
   "I couldn't find the answer in the provided documents."
4. Be clear and concise.
5. Mention the source file if relevant.

========================
CONTEXT
========================

{context}

========================
QUESTION
========================

{query}

========================
ANSWER
========================
"""

        return prompt