"""
CRUD actions for statistics
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session
from api.games import models as game_models


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
    stats = {
        "wins": 0,
        "losses": 0,
        "win_ratio": 0.0,
        "goals_for": 0,
        "goals_against": 0,
        "goal_difference": 0,
    }
    # iterate over each game and update stats
    for game in games_played_by_team:
        # depending on which team is the one checking, setting the values of goals scored and perceived
        goals_scored_in_game = getattr(
            game,
            (
                "first_team_goals"
                if game.first_team_id == team_id
                else "second_team_goals"
            ),
        )
        goals_perceived_in_game = getattr(
            game,
            (
                "second_team_goals"
                if game.first_team_id == team_id
                else "first_team_goals"
            ),
        )

        # given there is no draw
        if goals_scored_in_game > goals_perceived_in_game:
            stats["wins"] += 1
        else:
            stats["losses"] += 1
        stats["goals_for"] += goals_scored_in_game
        stats["goals_against"] += goals_perceived_in_game
    stats["goal_difference"] = stats["goals_for"] - stats["goals_against"]
    win_percentage = stats["wins"] / (stats["wins"] + stats["losses"])

    stats["win_ratio"] = float(f"{win_percentage:.2f}")
    return stats
