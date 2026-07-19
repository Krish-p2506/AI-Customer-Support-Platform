from fastapi import FastAPI

app = FastAPI(
    title="AI Customer Support Platform",
    description="Enterprise-grade AI-powered customer support platform",
    version="1.0.0"
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "AI Customer Support Platform Running"
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy"
    }