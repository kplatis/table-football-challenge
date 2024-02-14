from api.games.models import Game
from api.statistics.calculator import calculate_stats_for_teams_and_players


def test_calculator_for_teams_and_players(test_main_database):
    games = test_main_database.query(Game).all()
    test = calculate_stats_for_teams_and_players(games=games)
