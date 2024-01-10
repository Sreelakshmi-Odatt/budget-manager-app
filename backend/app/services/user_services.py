from sqlalchemy.orm import Session

from app.models.user.schemas import ResponseUser, RequestUser
from app.models.user.user import User
import bcrypt


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()


def create_user(db: Session, user: RequestUser):
    hashed_password = hash_password(user.password)
    _user = User(username=user.username, email=user.email, password_hash=hashed_password)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    user.user_id = _user.user_id
    user.password = hashed_password
    return ResponseUser(is_success=True, message="User created successfully!", result=user)


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_user_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
