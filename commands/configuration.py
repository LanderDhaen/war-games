import discord
from discord import app_commands
from discord.ext import commands

from core.check import requires_admin
from core.context import get_interaction_guild
from services.configuration import create_configuration, get_configuration


class Configuration(
    commands.GroupCog, group_name="server", description="Manage your server for War Games."
):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="configure", description="Update the server configuration for War Games."
    )
    @app_commands.describe(
        host_role="The role that will be assigned to hosts.",
        participant_role="The role that will be assigned to participants.",
        game_channel="The channel where games will be posted.",
        results_channel="The channel where game results will be posted.",
    )
    @app_commands.rename(
        host_role="host-role",
        participant_role="participant-role",
        game_channel="game-channel",
        results_channel="results-channel",
    )
    @app_commands.default_permissions(administrator=True)
    @app_commands.guild_only()
    @requires_admin()
    async def setup_server(
        self,
        interaction: discord.Interaction,
        host_role: discord.Role,
        participant_role: discord.Role,
        game_channel: discord.TextChannel,
        results_channel: discord.TextChannel,
    ) -> None:

        await interaction.response.defer()

        interaction_guild = get_interaction_guild(interaction)
        interaction_user = interaction.user

        await create_configuration(
            guild_id=interaction_guild.id,
            interaction_user_id=interaction_user.id,
            host_role_id=host_role.id,
            participant_role_id=participant_role.id,
            game_channel_id=game_channel.id,
            results_channel_id=results_channel.id,
        )

        embed = discord.Embed(
            title="Server Configured",
            description=(
                f"The following settings have been updated in **{interaction_guild.name}**:"
            ),
            colour=discord.Colour.green(),
        )
        embed.add_field(
            name="The role that will be assigned to hosts.", value=host_role.mention, inline=False
        )
        embed.add_field(
            name="The role that will be assigned to participants.",
            value=participant_role.mention,
            inline=False,
        )
        embed.add_field(
            name="The channel where games will be posted.", value=game_channel.mention, inline=False
        )
        embed.add_field(
            name="The channel where game results will be posted.",
            value=results_channel.mention,
            inline=False,
        )

        await interaction.followup.send(embed=embed)

    @app_commands.command(
        name="info", description="Display the server configuration for War Games."
    )
    @app_commands.default_permissions(administrator=True)
    @app_commands.guild_only()
    @requires_admin()
    async def display_configuration(self, interaction: discord.Interaction) -> None:

        await interaction.response.defer()

        interaction_guild = get_interaction_guild(interaction)
        configuration = await get_configuration(interaction_guild.id)

        host_role = interaction_guild.get_role(configuration.host_role_id)
        participant_role = interaction_guild.get_role(configuration.participant_role_id)
        game_channel = interaction_guild.get_channel(configuration.game_channel_id)
        results_channel = interaction_guild.get_channel(configuration.results_channel_id)
        updated_by = interaction_guild.get_member(configuration.modified_by)

        embed = discord.Embed(
            title="Server Information",
            description=f"The following settings have been saved in **{interaction_guild.name}**:",
            colour=discord.Colour.blue(),
        )
        embed.add_field(
            name="The role that will be assigned to hosts.",
            value=host_role.mention if host_role else "*This role has been deleted*",
            inline=False,
        )
        embed.add_field(
            name="The role that will be assigned to participants.",
            value=participant_role.mention if participant_role else "*This role has been deleted*",
            inline=False,
        )
        embed.add_field(
            name="The channel where games will be posted.",
            value=game_channel.mention if game_channel else "*This channel has been deleted*",
            inline=False,
        )
        embed.add_field(
            name="The channel where game results will be posted.",
            value=results_channel.mention if results_channel else "*This channel has been deleted*",
            inline=False,
        )

        if updated_by is not None:
            embed.set_footer(icon_url=updated_by.display_avatar.url , text=f"Last updated by {updated_by.display_name} on {configuration.modified_at.strftime("%b %#d, %Y")}.")

        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Configuration(bot))
