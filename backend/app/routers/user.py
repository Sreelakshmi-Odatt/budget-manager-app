from fastapi import APIRouter, HTTPException, Depends
from ..auth.auth_bearer import JWTBearer
from ..config import SessionLocal
from sqlalchemy.orm import Session

from ..models.user.schemas import RequestUser
from ..services.user_services import (

    get_user, create_user
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(JWTBearer())],
    responses={404: {"message": "Hello"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_user_endpoint(request: RequestUser, db: Session = Depends(get_db)):
    _user = get_user(db, request.user_id)
    if _user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user=request)


@router.get("/{user_id}")
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    _user = get_user(db, user_id)
    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return _user
