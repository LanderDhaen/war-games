from data.database import utc_now
from data.models.guild import Guild, GuildModel
from errors.guild import MissingGuild


async def get_guild(guild_id: int) -> GuildModel:

    guild = await Guild.select().where(Guild.guild_id == guild_id).first()

    if guild is None:
        raise MissingGuild()

    return GuildModel(**guild)


async def create_guild(guild_id: int) -> GuildModel:

    rows = (
        await Guild.insert(Guild(guild_id=guild_id))
        .on_conflict(
            target=Guild.guild_id,
            action="DO UPDATE",
            values=[Guild.modified_at, (Guild.joined_at, utc_now()), (Guild.left_at, None)],
        )
        .returning(*Guild.all_columns())
    )

    return GuildModel(**rows[0])


async def remove_guild(guild_id: int) -> GuildModel | None:

    rows = (
        await Guild.update({Guild.left_at: utc_now()})
        .where(Guild.guild_id == guild_id)
        .returning(*Guild.all_columns())
    )

    return GuildModel(**rows[0]) if rows else None
