from tortoise import fields
from tortoise.models import Model
from enum import IntEnum


class BetState(IntEnum):
    PENDING = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Bet(Model):
    uuid = fields.UUIDField(pk=True)
    amount = fields.FloatField(null=True)
    state = fields.IntEnumField(BetState)
    event_uuid = fields.CharField(null=True, max_length=255)

    def __str__(self):
        return f'{self.uuid} ({self.state})'

    class Meta:
        ordering = ['amount']
