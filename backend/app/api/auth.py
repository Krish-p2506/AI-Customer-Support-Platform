from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.schemas.user import UserResponse

from app.database.dependencies import get_db
from app.services.auth_service import create_user

from fastapi import HTTPException

from app.schemas.user import UserLogin
from app.schemas.user import Token

from app.services.auth_service import login_user
from app.dependencies.auth import get_current_user
from app.schemas.user import CurrentUser
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        db=db,
        email=user.email,
        password=user.password
    )

@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    token = login_user(
        db,
        user.email,
        user.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.get(
    "/me",
    response_model=CurrentUser
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user