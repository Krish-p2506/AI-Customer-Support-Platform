from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password
from app.core.security import verify_password
from app.core.security import create_access_token

def create_user(
    db: Session,
    email: str,
    password: str
):
    hashed_pw = hash_password(password)

    user = User(
        email=email,
        hashed_password=hashed_pw
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(
    db: Session,
    email: str,
    password: str
):
    print("STEP 1")

    user = db.query(User).filter(
        User.email == email
    ).first()

    print("STEP 2", user)

    if not user:
        return None

    print("STEP 3")

    result = verify_password(
        password,
        user.hashed_password
    )

    print("STEP 4", result)

    if not result:
        return None

    print("STEP 5")

    token = create_access_token(
        {"sub": user.email}
    )

    print("STEP 6")

    return token