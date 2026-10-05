from discord import Guild, Interaction, app_commands


def get_interaction_guild(interaction: Interaction) -> Guild:

    guild = interaction.guild

    if guild is None:
        raise app_commands.NoPrivateMessage()

    return guild
