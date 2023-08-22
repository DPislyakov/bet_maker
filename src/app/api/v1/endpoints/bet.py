import datetime
import time
from typing import List
import aioredis

from fastapi import APIRouter

from app.core.exceptions import NotFoundError, InvalidDataError
from app.config import common_config

from app.models.tortoise.bet import BetState
from app.selectors.bet import BetSelector
from app.services.bet import BetService
from app.schemas.bet import (BetOutSchema, BetCreateSchema)

router = APIRouter()


@router.post('', response_model=BetOutSchema)
async def bet_create(
        bet_detail: BetCreateSchema
):
    redis = await aioredis.create_redis_pool(f'redis://{common_config.REDIS_HOST}:{common_config.REDIS_PORT}')
    if await redis.hget(common_config.EVENT_ACTIVE_HM, bet_detail.event_uuid):
        bet = await BetService().create(amount=bet_detail.amount,
                                        event_uuid=bet_detail.event_uuid,
                                        state=BetState.PENDING)
        if bet is None:
            raise InvalidDataError(detail=f"Event data is invalided.")
    else:
        raise InvalidDataError(detail=f"Event already is closed.")
    redis.close()
    await redis.wait_closed()
    return bet


@router.get('', response_model=List[BetOutSchema])
async def bets_get():
    bets = await BetSelector.list_get()
    for bet in bets:
        if bet.state == BetState.PENDING:
            redis = await aioredis.create_redis_pool(f'redis://{common_config.REDIS_HOST}:{common_config.REDIS_PORT}')
            state = await redis.hget(common_config.EVENT_FINISHED_HM, bet.event_uuid)
            if state:
                bet.state = int(state.decode('utf-8')) if not isinstance(state, str) else int(state)
                await bet.save()
    return bets
