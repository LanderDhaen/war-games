from discord import app_commands


class ExpectedError(app_commands.AppCommandError):
    """Base class for errors which can be displayed directly to a user."""

    title: str
    description: str

    def __init__(self):
        super().__init__(self.description)
