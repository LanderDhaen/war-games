import logging
from typing import Literal

import discord
from discord.ext import commands

from errors.expected import ExpectedError

from bot import WarGamesBot
from config import TOKEN
from services.guild import create_guild, get_guild, remove_guild


bot = WarGamesBot()
logger = logging.getLogger(__name__)


@bot.command(name="sync")
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, scope: Literal["global", "guild"] = "guild"):

    if ctx.guild is None:
        return await ctx.send("This command can only be used in a guild.")

    if scope == "guild":
        bot.tree.copy_global_to(guild=ctx.guild)
        synced = await bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"{len(synced)} command(s) synced for {ctx.guild.name}.")
    elif scope == "global":
        synced = await bot.tree.sync()
        await ctx.send(f"{len(synced)} command(s) synced globally.")


@bot.event
async def on_guild_join(interaction_guild: discord.Guild) -> None:
    guild = await create_guild(interaction_guild.id)

    logger.info(f"Guild {interaction_guild.id} joined at {guild.joined_at}.")


@bot.event
async def on_guild_remove(interaction_guild: discord.Guild) -> None:
    guild = await remove_guild(interaction_guild.id)

    if guild is None:
        logger.warning(f"Guild {interaction_guild.id} wasn't found when leaving.")

    else:
        logger.info(f"Guild {interaction_guild.id} left at {guild.left_at}.")


if TOKEN is None:
    raise RuntimeError("TOKEN environment variable is not set.")

if __name__ == "__main__":
    bot.run(TOKEN, root_logger=True)
