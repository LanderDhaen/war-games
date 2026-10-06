import logging

import discord
from discord import app_commands
from discord.ext import commands

from errors.expected import ExpectedError

logger = logging.getLogger(__name__)


class WarGamesBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.none()
        intents.members = True
        intents.messages = True
        intents.message_content = True
        intents.guilds = True
        super().__init__(command_prefix="!", intents=intents, tree_cls=WarGamesCommandTree)

    async def setup_hook(self) -> None:
        await self.load_extension("commands.configuration")


class WarGamesCommandTree(app_commands.CommandTree):
    async def on_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.AppCommandError,
    ) -> None:

        if interaction.command is None:
            return logger.error(
                "An error occurred while executing an unknown command.", exc_info=error
            )

        match error:
            case ExpectedError():
                title = error.title
                description = error.description

            case app_commands.NoPrivateMessage():
                title = "What happened here?"
                description = f"Commands cannot be used in private messages."

            case app_commands.BotMissingPermissions():
                title = "What happened here?"
                description = f"The bot is missing the following permissions to execute `/{interaction.command.qualified_name}`: {', '.join(error.missing_permissions)}."

            case app_commands.CommandInvokeError():
                title = "What happened here?"
                description = (
                    f"Something went wrong while executing `/{interaction.command.qualified_name}`."
                )

                logger.error(description, exc_info=error.original)

            case _:
                title = "What happened here?"
                description = (
                    f"Something went wrong while executing `/{interaction.command.qualified_name}`."
                )

                logger.error(description, exc_info=error)

        embed = discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.red(),
        )

        try:
            if interaction.response.is_done():
                await interaction.followup.send(embed=embed, ephemeral=True)
            else:
                await interaction.response.send_message(embed=embed, ephemeral=True)
        except discord.HTTPException:
            logger.exception("Failed to send application command error response")
