from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class ExpenseCategory(Base):

    tableName = "ExpenseCategory"

    expense_id = Column(Integer, primary_key=True)
    expense_name = Column(String, unique=True)
