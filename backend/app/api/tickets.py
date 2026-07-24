from fastapi import HTTPException
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.dependencies.auth import get_current_user

from app.models.user import User
from app.services.ticket_service import get_user_tickets
from app.services.ticket_service import get_ticket_by_id

from app.schemas.ticket import TicketUpdate
from app.services.ticket_service import update_ticket_status

from app.schemas.ticket import (
    TicketCreate,
    TicketResponse
)

from app.services.ticket_service import create_ticket

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)



@router.post(
    "",
    response_model=TicketResponse
)
def create_new_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_ticket(
        db=db,
        title=ticket.title,
        description=ticket.description,
        user_id=current_user.id
    )
@router.get(
    "",
    response_model=list[TicketResponse]
)
def get_tickets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_tickets(
        db,
        current_user.id
    )
@router.get(
    "/{ticket_id}",
    response_model=TicketResponse
)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = get_ticket_by_id(
        db,
        ticket_id,
        current_user.id
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket

@router.patch(
    "/{ticket_id}",
    response_model=TicketResponse
)
def update_ticket(
    ticket_id: int,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = update_ticket_status(
        db,
        ticket_id,
        current_user.id,
        ticket_data.status
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket