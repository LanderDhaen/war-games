from typing import Optional

from asyncpg import IntegrityConstraintViolationError

from data.models.tournament import (
    Tournament,
    TournamentConstraints,
    TournamentModel,
)
from errors.tournament import DuplicateTournamentName, InvalidTournamentTeamSize, MissingTournament


async def create_tournament(
    guild_id: int,
    interaction_user_id: int,
    name: str,
    team_size: int,
    description: Optional[str] = None,
) -> TournamentModel:

    try:
        rows = await Tournament.insert(
            Tournament(
                created_by=interaction_user_id,
                modified_by=interaction_user_id,
                name=name,
                team_size=team_size,
                description=description,
                guild=guild_id,
            )
        ).returning(
            Tournament.id,
            Tournament.created_at,
            Tournament.modified_at,
            Tournament.created_by,
            Tournament.modified_by,
            Tournament.name,
            Tournament.team_size,
            Tournament.description,
            Tournament.status,
        )
    except IntegrityConstraintViolationError as error:
        constraint_name = error.as_dict().get("constraint_name")

        match constraint_name:
            case TournamentConstraints.UNIQUE_TOURNAMENT_NAME_GUILD:
                raise DuplicateTournamentName(tournament_name=name) from error

            case TournamentConstraints.CHECK_TEAM_SIZE_RANGE:
                raise InvalidTournamentTeamSize() from error

            case _:
                raise

    return TournamentModel(**rows[0])

async def get_tournament(guild_id: int, tournament_name: str) -> TournamentModel:
    tournament = (
        await Tournament.select(
            Tournament.id,
            Tournament.created_at,
            Tournament.modified_at,
            Tournament.created_by,
            Tournament.modified_by,
            Tournament.name,
            Tournament.team_size,
            Tournament.description,
            Tournament.status,
        )
        .where((Tournament.guild == guild_id) & (Tournament.name == tournament_name))
        .output(nested=True)
        .first()
    )

    if not tournament:
        raise MissingTournament(tournament_name=tournament_name)

    return TournamentModel(**tournament)

async def get_tournaments(guild_id: int) -> list[TournamentModel]:

    tournaments = (
        await Tournament.select(
            Tournament.id,
            Tournament.created_at,
            Tournament.modified_at,
            Tournament.created_by,
            Tournament.modified_by,
            Tournament.name,
            Tournament.team_size,
            Tournament.description,
            Tournament.status,
        )
        .where(Tournament.guild == guild_id)
    )

    return [TournamentModel(**tournament) for tournament in tournaments]