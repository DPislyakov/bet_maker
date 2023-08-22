from typing import List
import aioredis

from fastapi import APIRouter

from app.core.exceptions import NotFoundError, InvalidDataError
from app.schemas.event import EventOutSchema, EventState
from app.config import common_config

router = APIRouter()


@router.get('', response_model=List[EventOutSchema])
async def events_get():
    result = list()
    redis = await aioredis.create_redis_pool(f'redis://{common_config.REDIS_HOST}:{common_config.REDIS_PORT}')
    hm_ = await redis.hgetall(common_config.EVENT_ACTIVE_HM)
    if hm_:
        for key, item in hm_.items():
            result.append(EventOutSchema(uuid=key.decode('utf-8') if not isinstance(key, str) else key,
                                         coefficient=item.decode('utf-8').split("-")[0] if not isinstance(key, str)
                                         else key.split("-")[0],
                                         deadline=item.decode('utf-8').split("-")[1] if not isinstance(key, str)
                                         else key.split("-")[1],
                                         state=EventState.NEW)
                          )
    redis.close()
    await redis.wait_closed()
    return result

