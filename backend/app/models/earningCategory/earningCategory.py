from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class EarningCategory(Base):

    tableName = "EarningCategory"

    earning_id = Column(Integer, primary_key=True)
    earning_name = Column(String, unique=True)
