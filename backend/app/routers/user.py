from fastapi import APIRouter, HTTPException, Depends

from ..config import SessionLocal
from sqlalchemy.orm import Session
# from ..models.user.schemas import RequestUser
from ..services.user_services import (

    get_user
)

router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_id}")
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    _user = get_user(db, user_id)
    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return _user

