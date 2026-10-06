from discord import Permissions

GREEN_TICK = "<:check:1556765090018099291>"
RED_CROSS = "<:no:1556768039117262858>"


def format_permission(permission: str) -> str:
    """
    Convert a Discord permission name into a human-readable label.

    Args:
        permission: The Discord permission name.

    Returns:
        The formatted permission label.
    """

    return permission.replace("_", " ").title()


def format_permissions(
    bot_permissions: Permissions,
    required_permissions: Permissions,
) -> str:
    """
    Format required Discord permissions and indicate whether the bot has them.

    Args:
        bot_permissions: The permissions currently available to the bot.
        required_permissions: The permissions required by the bot.

    Returns:
        A human-readable list of required permissions and their status.
    """

    return "\n".join(
        f"{GREEN_TICK if getattr(bot_permissions, permission) else RED_CROSS} "
        f"{format_permission(permission)}"
        for permission, required in required_permissions
        if required
    )
