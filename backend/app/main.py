from fastapi import FastAPI
from app.core.config import settings
from app.database.connection import engine
from app.database.base import Base
from app.models.user import User
from app.api.auth import router as auth_router
from app.models.ticket import Ticket
from app.api.tickets import router as ticket_router
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(auth_router)
app.include_router(ticket_router)

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