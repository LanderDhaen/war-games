from discord import Guild, Interaction, Role, app_commands

from errors.configuration import MissingHostRole


def get_interaction_guild(interaction: Interaction) -> Guild:

    guild = interaction.guild

    if guild is None:
        raise app_commands.NoPrivateMessage()

    return guild


def get_host_role(guild: Guild, host_role_id: int) -> Role:

    host_role = guild.get_role(host_role_id)

    if host_role is None:
        raise MissingHostRole()

    return host_role
