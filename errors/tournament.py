from data.models.tournament import MAX_TEAM_SIZE, MIN_TEAM_SIZE
from errors.expected import ExpectedError


class DuplicateTournamentName(ExpectedError):
    """Raised when a tournament name is already in use in a server."""

    title = "Duplicate Tournament"

    def __init__(self, tournament_name: str):
        self.description = (
            f"A tournament with the name `{tournament_name}` already exists in this server."
        )
        super().__init__()


class InvalidTournamentTeamSize(ExpectedError):
    """Raised when a tournament team size is invalid."""

    title = "Invalid Tournament"
    description = f"A tournament team size must be between {MIN_TEAM_SIZE} and {MAX_TEAM_SIZE}."


class MissingTournament(ExpectedError):
    """Raised when a tournament can't be found in the current server."""

    title = "Missing Tournament"

    def __init__(self, tournament_name: str):
        self.description = (
            f"A tournament with the name `{tournament_name}` doesn't exist in this server."
        )
        super().__init__()
