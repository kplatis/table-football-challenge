"""
CRUD actions for statistics
"""

from typing import Dict
from sqlalchemy import or_
from sqlalchemy.orm import Session
from api.games import models as game_models
from api.statistics.schemas import Stats
from api.teams import models as team_models
from api.players import models as player_models
from api.statistics.calculator import (
    calculate_stats_for_player,
    calculate_stats_for_team,
)


def get_statistics_for_team(team_id: int, db: Session):
    """
    Returns the statistics for a single team
    """
    games_played_by_team = (
        db.query(game_models.Game)
        .filter(
            or_(
                game_models.Game.first_team_id == team_id,
                game_models.Game.second_team_id == team_id,
            )
        )
        .all()
    )
    return calculate_stats_for_team(games=games_played_by_team, team_id=team_id)


def get_statistics_of_all_teams(db: Session):
    """
    Returns the statistics of all teams
    """

    all_teams = db.query(team_models.Team).all()
    team_to_stats = {}
    for team in all_teams:
        statistics = get_statistics_for_team(team_id=team.id, db=db)
        team_to_stats[team.id] = statistics
    return team_to_stats


def get_statistics_of_all_players(team_ids_to_stats: Dict[int, Stats], db: Session):
    """
    Given a dictionary of TeamID => stats, calculates the statistics of all players
    """

    all_players = db.query(player_models.Player).all()
    all_player_stats = []
    # iterating over all players
    for player in all_players:
        # create a list of all the team ids that the player took part in
        team_ids_of_player = [team.id for team in player.first_player_teams] + [
            team.id for team in player.second_player_teams
        ]
        # calculate the statistics of the player
        player_stats = calculate_stats_for_player(
            teams_of_player=team_ids_of_player,
            team_ids_to_stats=team_ids_to_stats,
        )
        player_stats["name"] = player.name
        # append in the list
        all_player_stats.append(player_stats)
    return all_player_stats
