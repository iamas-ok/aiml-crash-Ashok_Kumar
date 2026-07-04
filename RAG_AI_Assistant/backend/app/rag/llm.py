from groq import Groq

from app.core.config import settings


class LLMClient:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_response(
        self,
        prompt: str,
        model_name: str,
    ):

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