from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Groq
    GROQ_API_KEY: str

    # Chroma
    CHROMA_DB_PATH: str = "chroma_db"

    # Embedding Model
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    # Default LLM
    DEFAULT_MODEL: str = "openai/gpt-oss-20b"

    class Config:
        env_file = ".env"


settings = Settings()