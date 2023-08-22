from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.tortoise.bet import Bet


Tortoise.init_models(["app.models.tortoise.bet"],
                     "models")

Bet_Pydantic = pydantic_model_creator(
    Bet,
    name="Bet"
)
