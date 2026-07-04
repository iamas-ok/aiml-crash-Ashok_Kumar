from app.core.config import settings

print("Secret Key :", settings.SECRET_KEY)
print("Default Model :", settings.DEFAULT_MODEL)
print("Embedding Model :", settings.EMBEDDING_MODEL)
print("Chroma Path :", settings.CHROMA_DB_PATH)