from typing import Optional
from pydantic import BaseModel
import decimal
from enum import IntEnum


class EventState(IntEnum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class EventOutSchema(BaseModel):
    uuid: str
    coefficient: Optional[decimal.Decimal]
    deadline: Optional[int]
    state: Optional[int]

