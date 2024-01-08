

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    password_hash = Column(String(29), nullable=False)
