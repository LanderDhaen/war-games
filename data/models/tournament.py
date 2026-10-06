from enum import StrEnum, auto

from piccolo.columns import ForeignKey, SmallInt, OnDelete, Text, Varchar
from piccolo.constraints import Check, Unique
from piccolo.table import Table

from data.database import IdentityMixin, AuditMixin
from data.models.base import AuditModel, IdentityModel
from data.models.guild import Guild


MIN_TEAM_SIZE = 1
MAX_TEAM_SIZE = 50


class TournamentConstraints(StrEnum):
    UNIQUE_TOURNAMENT_NAME_GUILD = "unique_tournament_name_guild"
    CHECK_TEAM_SIZE_RANGE = "team_size_range"


class TournamentStatus(StrEnum):
    PENDING = auto()
    ACTIVE = auto()
    FINISHED = auto()

    def __str__(self) -> str:
        return self.value.title()


class Tournament(IdentityMixin, AuditMixin, Table):
    name = Varchar(length=50)
    description = Varchar(length=512, null=True, default=None)
    team_size = SmallInt()
    status = Varchar(
        choices=TournamentStatus,
        default=TournamentStatus.PENDING,
    )

    guild = ForeignKey(references=Guild, null=False, on_delete=OnDelete.restrict)

    unique_tournament_name_guild = Unique(
        [name, guild], name=TournamentConstraints.UNIQUE_TOURNAMENT_NAME_GUILD
    )
    team_size_range = Check(
        (team_size >= MIN_TEAM_SIZE) & (team_size <= MAX_TEAM_SIZE),
        name=TournamentConstraints.CHECK_TEAM_SIZE_RANGE,
    )


class TournamentModel(IdentityModel, AuditModel):
    name: str
    description: str | None
    team_size: int
    status: TournamentStatus
