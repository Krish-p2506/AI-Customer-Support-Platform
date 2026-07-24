from pydantic import BaseModel
from app.models.enums import TicketStatus


class TicketCreate(BaseModel):
    title: str
    description: str


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config:
        from_attributes = True
class TicketUpdate(BaseModel):
    status: TicketStatus