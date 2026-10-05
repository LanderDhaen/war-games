from errors.expected import ExpectedError


class MissingGuild(ExpectedError):
    """Raised when a guild is not found in the database."""

    title = "Missing Guild"
    description = "This guild doesn't exist."
