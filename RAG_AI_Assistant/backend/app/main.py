from fastapi import FastAPI

app = FastAPI(
    title="RAG AI Assistant API",
    description="Production-ready RAG AI Assistant Backend",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to RAG AI Assistant API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }