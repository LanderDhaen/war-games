from discord import Interaction
from discord.app_commands import Choice

from core.context import get_interaction_guild
from data.models.tournament import TournamentFilters, TournamentStatus
from services.tournament import get_tournaments


def tournament_autocomplete(statuses: list[TournamentStatus] | None = None):
    async def autocomplete(
        interaction: Interaction,
        current: str,
    ) -> list[Choice[str]]:
        guild = get_interaction_guild(interaction)

        filters = TournamentFilters(
            search=current.casefold(),
            status=statuses,
            limit=25,
            offset=0,
        )

        tournaments = await get_tournaments(guild.id, filters)

        return [
            Choice(
                name=f"{tournament.name} • {tournament.team_size}v{tournament.team_size}",
                value=tournament.name,
            )
            for tournament in tournaments
        ]

    return autocomplete
