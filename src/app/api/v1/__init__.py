from fastapi import APIRouter
from .endpoints import (
    bet as api_bet,
    event as api_event,
)

api_router = APIRouter()
api_router.include_router(api_bet.router, prefix='/bets', tags=["Bets"])
api_router.include_router(api_event.router, prefix='/events', tags=["Events"])

