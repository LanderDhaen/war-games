from piccolo.columns import (
    BigInt,
    ForeignKey,
    OnDelete,
)
from piccolo.table import Table

from data.database import IdentityMixin, MetaMixin
from data.models.guild import Guild


class Configuration(IdentityMixin, MetaMixin, Table):
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
