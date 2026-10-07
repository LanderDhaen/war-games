from discord import Interaction
from discord.app_commands import Choice

from core.context import get_interaction_guild
from data.models.tournament import TournamentFilters
from services.tournament import get_tournaments


async def tournament_autocomplete(interaction: Interaction, current: str):

    interaction_guild = get_interaction_guild(interaction)

    filters = TournamentFilters(search=current.casefold(), limit=25, offset=0)

    tournaments = await get_tournaments(interaction_guild.id, filters)

    return [
        Choice(
            name=f"tournament.name • {tournament.team_size}v{tournament.team_size}",
            value=tournament.name,
        )
        for tournament in tournaments
    ]
