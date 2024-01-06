from sqlalchemy import Column, String, Integer

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    tableName = "User"


user_id = Column(Integer, primary_key=True)
username = Column(String, unique=True)
password = Column(String)
email = Column(String, unique=True)

