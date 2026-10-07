from discord import Interaction
from discord.app_commands import Choice

from core.context import get_interaction_guild
from services.tournament import get_tournaments


async def tournament_autocomplete(interaction: Interaction, current: str):

    interaction_guild = get_interaction_guild(interaction)

    tournaments = await get_tournaments(interaction_guild.id)

    return [
        Choice(name=tournament.name, value=tournament.name)
        for tournament in tournaments[:25]
        if current.casefold() in tournament.name.casefold()
    ]