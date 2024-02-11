from typing import Dict, List
from api.games.models import Game
from api.statistics.schemas import StatisticsByTeamOrPlayer


def calculate_stats_for_team(games: Game, team_id: int):
    """
    Calculates the statistics of all games
    """
    stats = {
        "wins": 0,
        "losses": 0,
        "win_ratio": 0.0,
        "goals_for": 0,
        "goals_against": 0,
        "goals_difference": 0,
    }
    # iterate over each game and update stats
    for game in games:
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
    stats["goals_difference"] = stats["goals_for"] - stats["goals_against"]
    win_percentage = stats["wins"] / (stats["wins"] + stats["losses"])

    stats["win_ratio"] = float(f"{win_percentage:.2f}")
    return stats


def calculate_stats_for_player(
    teams_of_player: List[int], team_ids_to_stats: Dict[int, Dict]
):
    """
    Calculates the stats for a player, given a list of the IDs of the teams that the player
    took part in (teams_of_players) and a dictionary with the Ids of the teams and the stats
    """
    stats = {
        "wins": 0,
        "losses": 0,
        "win_ratio": 0.0,
        "goals_for": 0,
        "goals_against": 0,
        "goals_difference": 0,
    }
    for team_id in teams_of_player:
        team_stats = team_ids_to_stats[team_id]
        stats["wins"] += team_stats["wins"]
        stats["losses"] += team_stats["losses"]
        stats["goals_for"] += team_stats["goals_for"]
        stats["goals_against"] += team_stats["goals_against"]
        stats["goals_difference"] += team_stats["goals_difference"]
    win_percentage = stats["wins"] / (stats["wins"] + stats["losses"])
    stats["win_ratio"] = float(f"{win_percentage:.2f}")
    return stats
