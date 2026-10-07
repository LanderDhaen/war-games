from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands

from core.autocomplete import tournament_autocomplete
from core.check import requires_host_role
from core.context import get_interaction_guild
from core.embed import build_tournament_embed
from services.tournament import create_tournament, get_tournament
from data.models.tournament import TournamentStatus


class Tournament(
    commands.GroupCog, group_name="tournament", description="Manage your War Games tournaments."
):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="schedule", description="Schedule a new War Games tournament.")
    @app_commands.describe(
        name="The name of the tournament.",
        team_size="The size of each team in the tournament.",
        description="The description of the tournament.",
    )
    @app_commands.rename(team_size="team-size")
    @app_commands.guild_only()
    @requires_host_role()
    async def schedule_tournament(
        self,
        interaction: discord.Interaction,
        name: discord.app_commands.Range[str, 1, 50],
        team_size: discord.app_commands.Range[int, 1, 50],
        description: Optional[discord.app_commands.Range[str, 1, 512]] = None,
    ) -> None:

        await interaction.response.defer()

        interaction_guild = get_interaction_guild(interaction)
        interaction_user = interaction.user

        tournament = await create_tournament(
            guild_id=interaction_guild.id,
            interaction_user_id=interaction_user.id,
            name=name,
            team_size=team_size,
            description=description,
        )

        embed = build_tournament_embed(
            tournament,
            title="Tournament Scheduled",
            description=f"A new War Games tournament has been scheduled in **{interaction_guild.name}**",
            color=discord.Color.green(),
        )

        await interaction.followup.send(embed=embed)

    @app_commands.command(name="info", description="Display the information for a War Games tournament")
    @app_commands.describe(tournament_name="The name of the tournament.")
    @app_commands.rename(tournament_name="tournament")
    @app_commands.autocomplete(tournament_name=tournament_autocomplete)
    @app_commands.guild_only()
    async def display_tournament(
        self,
        interaction: discord.Interaction,
        tournament_name: str,
    ) -> None:
        await interaction.response.defer()

        interaction_guild = get_interaction_guild(interaction)
        tournament = await get_tournament(interaction_guild.id, tournament_name)

        updated_by = interaction_guild.get_member(tournament.modified_by)

        match tournament.status:
            case TournamentStatus.PENDING:
                verb = "is scheduled" \
            
            case TournamentStatus.ACTIVE:
                verb = "is running"

            case TournamentStatus.FINISHED:
                verb = "was hosted"

            case _:
                verb = "is hosted"

        embed = build_tournament_embed(
            tournament,
            title="Tournament Information",
            description=f"The following War Games tournament {verb} in **{interaction_guild.name}**:",
            color=discord.Colour.blue(),
        )
       
        if updated_by is not None:
            embed.set_footer(icon_url=updated_by.display_avatar.url, text=f"Last updated by {updated_by.display_name} on {tournament.modified_at.strftime('%b %#d, %Y')}.")


        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Tournament(bot))
