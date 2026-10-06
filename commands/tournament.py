from typing import Optional

import discord
from discord import app_commands
from discord.permissions import Permissions
from discord.ext import commands

from core.check import requires_host_role
from core.context import get_interaction_guild
from services.tournament import create_tournament


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

        embed = discord.Embed(
            title="Tournament Scheduled",
            description=f"A new War Games tournament has been scheduled in **{interaction_guild.name}**",
            color=discord.Color.green(),
        )

        embed.add_field(name="Name", value=tournament.name, inline=False)

        embed.add_field(
            name="Description",
            value=description if description else "*This tournament has no description.*",
            inline=False,
        )

        embed.add_field(name="Format", value=f"{tournament.team_size}v{tournament.team_size}", inline=False)

        embed.add_field(name="Status", value=tournament.status, inline=False)

        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Tournament(bot))
