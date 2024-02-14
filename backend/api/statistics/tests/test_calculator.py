from api.games.models import Game
from api.statistics.calculator import calculate_stats_for_teams_and_players


def test_calculator_for_players(test_main_database):
    games = test_main_database.query(Game).all()
    _, players = calculate_stats_for_teams_and_players(games=games)
    assert players[1]["name"] == "Player1"
    assert players[1]["wins"] == 4
    assert players[1]["losses"] == 3
    assert players[1]["win_ratio"] == 0.57
    assert players[1]["goals_for"] == 20
    assert players[1]["goals_against"] == 11
    assert players[1]["goals_difference"] == 9

    assert players[2]["name"] == "Player2"
    assert players[2]["wins"] == 2
    assert players[2]["losses"] == 1
    assert players[2]["win_ratio"] == 0.67
    assert players[2]["goals_for"] == 7
    assert players[2]["goals_against"] == 6
    assert players[2]["goals_difference"] == 1

    assert players[3]["name"] == "Player3"
    assert players[3]["wins"] == 2
    assert players[3]["losses"] == 5
    assert players[3]["win_ratio"] == 0.29
    assert players[3]["goals_for"] == 10
    assert players[3]["goals_against"] == 21
    assert players[3]["goals_difference"] == -11

    assert players[4]["name"] == "Player4"
    assert players[4]["wins"] == 2
    assert players[4]["losses"] == 1
    assert players[4]["win_ratio"] == 0.67
    assert players[4]["goals_for"] == 7
    assert players[4]["goals_against"] == 6
    assert players[4]["goals_difference"] == 1


def test_calculator_for_teams(test_main_database):
    games = test_main_database.query(Game).all()
    teams, _ = calculate_stats_for_teams_and_players(games=games)

    assert teams[1]["wins"] == 1
    assert teams[1]["losses"] == 2
    assert teams[1]["win_ratio"] == 0.33
    assert teams[1]["goals_for"] == 6
    assert teams[1]["goals_against"] == 7
    assert teams[1]["goals_difference"] == -1

    assert teams[2]["wins"] == 2
    assert teams[2]["losses"] == 1
    assert teams[2]["win_ratio"] == 0.67
    assert teams[2]["goals_for"] == 7
    assert teams[2]["goals_against"] == 6
    assert teams[2]["goals_difference"] == 1

    assert teams[3]["wins"] == 3
    assert teams[3]["losses"] == 1
    assert teams[3]["win_ratio"] == 0.75
    assert teams[3]["goals_for"] == 14
    assert teams[3]["goals_against"] == 4
    assert teams[3]["goals_difference"] == 10

    assert teams[4]["wins"] == 1
    assert teams[4]["losses"] == 3
    assert teams[4]["win_ratio"] == 0.25
    assert teams[4]["goals_for"] == 4
    assert teams[4]["goals_against"] == 14
    assert teams[4]["goals_difference"] == -10
