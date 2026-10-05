from datetime import UTC, datetime

from piccolo.columns import (
    BigInt,
    Serial,
    Timestamptz,
)
from piccolo.columns.defaults.timestamptz import TimestamptzNow


def utc_now() -> datetime:
    return datetime.now(UTC)


class IdentityMixin:
    id = Serial(primary_key=True)


class TimestampMixin:
    created_at = Timestamptz(default=TimestamptzNow())
    modified_at = Timestamptz(default=TimestamptzNow(), auto_update=utc_now)

class AttributionMixing:
    created_by = BigInt()
    modified_by = BigInt()

class AuditMixin(TimestampMixin, AttributionMixing):
    pass