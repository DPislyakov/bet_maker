from app.selectors.utils import TortoiseSelector

from app.models.pydantic.bet import Bet_Pydantic
from app.models.tortoise.bet import Bet, BetState


class BetSelector(TortoiseSelector[Bet, Bet_Pydantic]):
    model = Bet
    pydantic_model = Bet_Pydantic
    id_field = 'uuid'

    @classmethod
    async def list_get_pending(cls):
        return await cls.list_get(state=BetState.PENDING)

    @classmethod
    async def list_get(cls, **kwargs):
        return await cls.list_get_as_qs(**kwargs)

    @classmethod
    def list_get_as_qs(cls, **kwargs):
        return cls.model.filter(**kwargs)
