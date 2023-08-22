from typing import Optional
from pydantic import BaseModel
import decimal

from app.models.pydantic.bet import Bet_Pydantic
from app.models.tortoise.bet import BetState


class BetCreateSchema(BaseModel):
    amount: Optional[float]
    event_uuid: Optional[str]


class BetOutSchema(Bet_Pydantic):
    pass

