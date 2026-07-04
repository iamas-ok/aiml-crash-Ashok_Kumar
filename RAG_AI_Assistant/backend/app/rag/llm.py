from groq import Groq

from app.core.config import settings
from app.rag.models import (
    SUPPORTED_MODELS,
    DEFAULT_MODEL,
)


class LLMClient:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_response(
            self,
            prompt: str,
            model_name: str = DEFAULT_MODEL,
        ):
        if model_name not in SUPPORTED_MODELS:
            raise ValueError(
                f"Unsupported model: {model_name}"
            )

        response = self.client.chat.completions.create(

            model=model_name,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            temperature=0.2,
        )

        return response.choices[0].message.content