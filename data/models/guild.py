from datetime import datetime

from piccolo.columns import (
    BigInt,
    Timestamptz,
)
from piccolo.columns.defaults.timestamptz import TimestamptzNow
from piccolo.table import Table

from data.database import MetaMixin

from data.models.base import MetaModel


class Guild(MetaMixin, Table):
    guild_id = BigInt(primary_key=True)
    joined_at = Timestamptz(default=TimestamptzNow())
    left_at = Timestamptz(null=True, default=None)


class GuildModel(MetaModel):
    guild_id: int
    joined_at: datetime
    left_at: datetime | None
