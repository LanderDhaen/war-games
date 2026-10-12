from data.models.tournament import MAX_TEAM_SIZE, MIN_TEAM_SIZE
from errors.expected import ExpectedError


class DuplicateTournamentName(ExpectedError):
    """Raised when a tournament name is already in use in a server."""

    title = "Duplicate Tournament"

    def __init__(self, tournament_name: str):
        self.description = (
            f"There's already a tournament with the name `{tournament_name}` in this server."
        )
        super().__init__()


class InvalidTournamentTeamSize(ExpectedError):
    """Raised when a tournament team size is invalid."""

    title = "Invalid Tournament"
    description = f"Team size must be between {MIN_TEAM_SIZE} and {MAX_TEAM_SIZE} players."


class MissingTournament(ExpectedError):
    """Raised when a tournament can't be found in the current server."""

    title = "Missing Tournament"

    def __init__(self, tournament_name: str):
        self.description = (
            f"There's no tournament with the name `{tournament_name}` in this server."
        )
        super().__init__()

class MissingScheduledTournament(ExpectedError):
    """Raised when a tournament can't be found in the current server."""

    title = "Missing Tournament"

    def __init__(self, tournament_name: str):
        self.description = (
            f"There's no scheduled tournament with the name `{tournament_name}` in this server."
        )
        super().__init__()

class MissingActiveTournament(ExpectedError):
    """Raised when a tournament can't be found in the current server."""

    title = "Missing Tournament"

    def __init__(self, tournament_name: str):
        self.description = (
            f"There's no active tournament with the name `{tournament_name}` in this server."
        )
        super().__init__()