import tortoise.exceptions

from app.services.utils import TortoiseService
from app.models.pydantic.bet import Bet_Pydantic
from app.models.tortoise.bet import Bet


class BetService(TortoiseService[Bet, Bet_Pydantic]):
    model = Bet
    pydantic_model = Bet_Pydantic

    async def create(self, **kwargs) -> Bet:
        try:
            return await super(BetService, self).create(**kwargs)
        except tortoise.exceptions.IntegrityError as e:
            print(e)

    async def update(self, **kwargs) -> Bet:
        return await super(BetService, self).update(**kwargs)
