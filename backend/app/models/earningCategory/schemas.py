from typing import Optional, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')


class EarningCategorySchema(BaseModel):
    earning_id: Optional[str] = None
    earning_name: Optional[str] = None

    class Config:
        from_attributes = True


class RequestEarningCategory(BaseModel):
    earning_id: int
    earning_name: str


class ResponseEarningCategory(BaseModel, Generic[T]):
    is_true: bool
    message: str
    result: Optional[T] = None
