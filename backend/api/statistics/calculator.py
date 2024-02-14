"""
Statitstic calculator functions
"""

from typing import List, Dict
from api.games.models import Game


def initialize_stats(name: str):
    """
    Initializes the statistics dictionary
    """
    return {
        name: name,
        "wins": 0,
        "losses": 0,
        "win_ratio": 0.0,
        "goals_for": 0,
        "goals_against": 0,
        "goals_difference": 0,
    }


def add_stats(
    stats: Dict[int, Dict], team_won: bool, goals_scored: int, goals_perceived: int
):
    """
    Adds the statistics to the existing dictionary based on whether the team won or not
    """
    total_matches = stats["wins"] + stats["losses"] + 1
    wins = stats["wins"] + 1 if team_won else stats["wins"]
    losses = stats["losses"] + 1 if not team_won else stats["losses"]
    win_ratio = wins / total_matches if total_matches > 0 else 0.0
    win_ratio = float(f"{win_ratio:.2f}")
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


def update_stats_of_team(
    name: str,
    teams_stats: Dict[int, Dict],
    team_id: int,
    team_won: bool,
    goals_scored: int,
    goals_perceived: int,
):
    """
    Calculates the statistics of a single team
    """
    # if team not in the dict, initialize
    if team_id not in teams_stats:
        teams_stats[team_id] = initialize_stats(name)
    # add the home team stats for this game
    teams_stats[team_id] = add_stats(
        teams_stats[team_id], team_won, goals_scored, goals_perceived
    )

    return teams_stats


def update_stats_of_player(
    name: str,
    players_stats: Dict[int, Dict],
    player_id: int,
    team_won: bool,
    goals_scored: int,
    goals_perceived: int,
):
    """
    Calculates the statistics of a single player
    """
    # calculating stats for first player of first team
    if player_id not in players_stats:
        players_stats[player_id] = initialize_stats(name)
    players_stats[player_id] = add_stats(
        players_stats[player_id],
        team_won,
        goals_scored,
        goals_perceived,
    )
    return players_stats


def calculate_stats_for_teams_and_players(games: List[Game]):
    """
    Given a list of games, calculates and returns the statistics for the teams and players that took part in the games
    """
    teams = {}
    players = {}
    for game in games:

        # TEAMS CALCULATION

        # calculate which team won
        home_team_goals = game.first_team_goals
        away_team_goals = game.second_team_goals
        home_team_won = home_team_goals > away_team_goals
        away_team_won = home_team_goals < away_team_goals

        # calculating stats for home team
        teams = update_stats_of_team(
            game.first_team.name,
            teams,
            game.first_team_id,
            home_team_won,
            home_team_goals,
            away_team_goals,
        )

        # calculating stats for away team
        teams = update_stats_of_team(
            game.second_team.name,
            teams,
            game.second_team_id,
            away_team_won,
            away_team_goals,
            home_team_goals,
        )

        # PLAYERS CALCULATION

        # calculating stats for first player of first team

        players = update_stats_of_player(
            game.first_team.first_player.name,
            players,
            game.first_team.first_player_id,
            home_team_won,
            home_team_goals,
            away_team_goals,
        )

        # calculating stats for second player of first team (if exists)
        if game.first_team.second_player_id:
            players = update_stats_of_player(
                game.first_team.second_player.name,
                players,
                game.first_team.second_player_id,
                home_team_won,
                home_team_goals,
                away_team_goals,
            )

        ###

        # calculating stats for first player of second team
        players = update_stats_of_player(
            game.second_team.first_player.name,
            players,
            game.second_team.first_player_id,
            away_team_won,
            away_team_goals,
            home_team_goals,
        )

        # calculating stats for second player of second team (if exists)
        if game.second_team.second_player_id:
            players = update_stats_of_player(
                game.second_team.second_player.name,
                players,
                game.second_team.second_player_id,
                away_team_won,
                away_team_goals,
                home_team_goals,
            )

    return teams, players
