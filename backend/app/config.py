from typing import List
from sqlalchemy.ext.declarative import declarative_base
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

config = Config(".env")

ROUTE_PREFIX_V1 = "/v1"

Base = declarative_base()

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default=[],
)


DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/budget_management_db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)


