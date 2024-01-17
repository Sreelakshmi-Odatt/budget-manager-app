from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class ExpenseCategorySchema(BaseModel):
    earning_id: Optional[str] = None
    earning_name: Optional[str] = None

    class Config:
        from_attributes = True


class RequestExpense (BaseModel):
    expense_id: int
    expense_name: str


class ResponseExpense (BaseModel, Generic[T]):
    is_true: bool
    message: str
    result: Optional[T] = None
