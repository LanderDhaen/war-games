from datetime import UTC, datetime

from piccolo.columns import (
    Serial,
    Timestamptz,
)
from piccolo.columns.defaults.timestamptz import TimestamptzNow


def utc_now() -> datetime:
    return datetime.now(UTC)


class IdentityMixin:
    id = Serial(primary_key=True)


class MetaMixin:
    created_at = Timestamptz(default=TimestamptzNow())
    modified_at = Timestamptz(default=TimestamptzNow(), auto_update=utc_now)
