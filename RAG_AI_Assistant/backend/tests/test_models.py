from app.rag.models import (
    SUPPORTED_MODELS,
    DEFAULT_MODEL,
)

print("Default Model:\n")

print(DEFAULT_MODEL)

print("\nSupported Models:\n")

for model_id, info in SUPPORTED_MODELS.items():

    print(model_id)

    print(info["name"])

    print(info["provider"])

    print("-" * 40)