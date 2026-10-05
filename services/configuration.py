from data.database import utc_now
from data.models.configuration import Configuration
from data.models.guild import Guild


async def create_configuration(
    guild_id: int,
    host_role_id: int,
    participant_role_id: int,
    game_channel_id: int,
    results_channel_id: int,
) -> None:
    async with Configuration._meta.db.transaction():
        await Guild.insert(Guild(guild_id=guild_id)).on_conflict(
            target=Guild.guild_id,
            action="DO NOTHING",
        )

        await Configuration.insert(
            Configuration(
                guild=guild_id,
                host_role_id=host_role_id,
                participant_role_id=participant_role_id,
                game_channel_id=game_channel_id,
                results_channel_id=results_channel_id,
            )
        ).on_conflict(
            target=Configuration.guild,
            action="DO UPDATE",
            values=[
                (Configuration.modified_at, utc_now()),
                Configuration.host_role_id,
                Configuration.participant_role_id,
                Configuration.game_channel_id,
                Configuration.results_channel_id,
            ],
        )
