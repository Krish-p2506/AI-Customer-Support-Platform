from sqlalchemy.orm import Session

from app.models.ticket import Ticket


def create_ticket(
    db: Session,
    title: str,
    description: str,
    user_id: int
):
    ticket = Ticket(
        title=title,
        description=description,
        user_id=user_id
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket
def get_user_tickets(
    db: Session,
    user_id: int
):
    return db.query(Ticket).filter(
        Ticket.user_id == user_id
    ).all()
def get_ticket_by_id(
    db: Session,
    ticket_id: int,
    user_id: int
):
    return db.query(Ticket).filter(
        Ticket.id == ticket_id,
        Ticket.user_id == user_id
    ).first()

def update_ticket_status(
    db: Session,
    ticket_id: int,
    user_id: int,
    status: str
):
    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id,
        Ticket.user_id == user_id
    ).first()

    if not ticket:
        return None

    ticket.status = status

    db.commit()
    db.refresh(ticket)

    return ticket