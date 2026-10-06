from piccolo.columns import (
    BigInt,
    ForeignKey,
    OnDelete,
)
from piccolo.table import Table

from data.database import IdentityMixin, AuditMixin
from data.models.base import IdentityModel, AuditModel
from data.models.guild import Guild


class Configuration(IdentityMixin, AuditMixin, Table):
    host_role_id = BigInt()
    participant_role_id = BigInt()
    game_channel_id = BigInt()
    results_channel_id = BigInt()
    guild = ForeignKey(
        references=Guild,
        null=False,
        on_delete=OnDelete.cascade,
        unique=True,
    )


class ConfigurationModel(IdentityModel, AuditModel):
    host_role_id: int
    participant_role_id: int
    game_channel_id: int
    results_channel_id: int
