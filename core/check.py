import discord
from discord import Member, app_commands

from core.context import get_host_role, get_interaction_guild
from errors.check import MissingAdministratorPermission, MissingHostRolePermission, MissingHostRolePermission
from services.configuration import get_configuration


def requires_admin():
    def predicate(interaction: discord.Interaction) -> bool:
        if not interaction.permissions.administrator:
            raise MissingAdministratorPermission()
        return True

    return app_commands.check(predicate)

def requires_host_role():
    async def predicate(interaction: discord.Interaction) -> bool:

        interaction_guild = get_interaction_guild(interaction)
        configuration = await get_configuration(interaction_guild.id)

        if not isinstance(interaction.user, Member):
            raise app_commands.NoPrivateMessage()

        host_role = get_host_role(interaction_guild, configuration.host_role_id)

        if host_role not in interaction.user.roles:
            raise MissingHostRolePermission()

        return True
    
    return app_commands.check(predicate)
