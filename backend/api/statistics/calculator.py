"""
Calculator functions for Statistics module
"""

from typing import Dict, List
from api.games.models import Game


def initialize_stats(name: str):
    return {
        name: name,
        "wins": 0,
        "losses": 0,
        "win_ratio": 0.0,
        "goals_for": 0,
        "goals_against": 0,
        "goals_difference": 0,
    }


def add_stats(stats, team_won: bool, goals_scored: int, goals_perceived: int):
    total_matches = stats["wins"] + stats["losses"] + 1
    wins = stats["wins"] + 1 if team_won else stats["wins"]
    losses = stats["losses"] + 1 if not team_won else stats["losses"]
    win_ratio = wins / total_matches if total_matches > 0 else 0.0
    goals_for = stats["goals_for"] + goals_scored
    goals_against = stats["goals_against"] + goals_perceived
    goals_difference = goals_for - goals_against
    return {
        **stats,
        "wins": wins,
        "losses": losses,
        "win_ratio": win_ratio,
        "goals_for": goals_for,
        "goals_against": goals_against,
        "goals_difference": goals_difference,
    }


def calculate_stats_for_teams_and_players(games: List[Game]):

    teams = {}
    players = {}
    for game in games:

        # TEAMS CALCULATION

        # calculate which team won
        home_team_goals = game.first_team_goals
        away_team_goals = game.second_team_goals
        home_team_won = home_team_goals > away_team_goals
        away_team_won = home_team_goals < away_team_goals
        # if team not in the dict, initialize
        if game.first_team_id not in teams:
            teams[game.first_team_id] = initialize_stats(game.first_team.name)
        # add the home team stats for this game
        teams[game.first_team_id] = add_stats(
            teams[game.first_team_id], home_team_won, home_team_goals, away_team_goals
        )
        # if team not in the dict, initialize
        if game.second_team_id not in teams:
            teams[game.second_team_id] = initialize_stats(game.second_team.name)
        # add the away team stats for this game
        teams[game.second_team_id] = add_stats(
            teams[game.second_team_id], away_team_won, away_team_goals, home_team_goals
        )

        # PLAYERS CALCULATION

        # calculating stats for first player of first team
        if game.first_team.first_player_id not in players:
            players[game.first_team.first_player_id] = initialize_stats(
                game.first_team.first_player.name
            )
        players[game.first_team.first_player_id] = add_stats(
            players[game.first_team.first_player_id],
            home_team_won,
            home_team_goals,
            away_team_goals,
        )

        if game.first_team.second_player_id:
            # calculating stats for first player of first team
            if game.first_team.second_player_id not in players:
                players[game.first_team.second_player_id] = initialize_stats(
                    game.first_team.second_player.name
                )
            players[game.first_team.second_player_id] = add_stats(
                players[game.first_team.second_player_id],
                home_team_won,
                home_team_goals,
                away_team_goals,
            )

        ###

        # calculating stats for first player of first team
        if game.second_team.first_player_id not in players:
            players[game.second_team.first_player_id] = initialize_stats(
                game.second_team.first_player.name
            )
        players[game.second_team.first_player_id] = add_stats(
            players[game.second_team.first_player_id],
            away_team_won,
            away_team_goals,
            home_team_goals,
        )

        if game.second_team.second_player_id:
            # calculating stats for first player of first team
            if game.second_team.second_player_id not in players:
                players[game.second_team.second_player_id] = initialize_stats(
                    game.second_team.second_player.name
                )
            players[game.second_team.second_player_id] = add_stats(
                players[game.second_team.second_player_id],
                away_team_won,
                away_team_goals,
                home_team_goals,
            )

        # TODO: do the same for players
    print(1)


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
    total_matches = stats["wins"] + stats["losses"]
    win_percentage = stats["wins"] / total_matches if total_matches > 0 else 0.0

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
    total_matches = stats["wins"] + stats["losses"]
    win_percentage = stats["wins"] / total_matches if total_matches > 0 else 0.0
    stats["win_ratio"] = float(f"{win_percentage:.2f}")
    return stats
