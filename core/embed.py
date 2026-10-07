from discord import Embed, Color
from data.models.tournament import TournamentModel


def build_tournament_embed(
    tournament: TournamentModel, title: str, description: str, color: Color
) -> Embed:

    embed = Embed(
        title=title,
        description=description,
        color=color,
    )

    embed.add_field(name="Name", value=tournament.name, inline=False)

    embed.add_field(
        name="Description",
        value=tournament.description
        if tournament.description
        else "*This tournament has no description.*",
        inline=False,
    )

    embed.add_field(
        name="Format", value=f"{tournament.team_size}v{tournament.team_size}", inline=False
    )

    embed.add_field(name="Status", value=tournament.status, inline=False)

    return embed
