from errors.expected import ExpectedError


class MissingConfiguration(ExpectedError):
    """Raised when a server does not have the required configuration to use a command."""

    title = "Missing Configuration"
    description = "This server is not yet configured. An administrator can use `/server configure` to get started."


class MissingHostRole(MissingConfiguration):
    """Raised when the host role doesn't exist in the server."""

    description = "The configured host role doesn't exist. An administrator can use `/server configure` to reconfigure it."
