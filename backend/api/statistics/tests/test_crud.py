# """
# Define unit tests for CRUD actions of statistics
# """

# from api.statistics.crud import (
#     get_statistics_of_team,
#     get_statistics_of_all_players,
#     get_statistics_dictionary_of_all_teams,
# )


# def test_statistics_retrieval_for_team_1(test_main_database):
#     """
#     Tests the CRUD action to retrieve statistics for a single team
#     """
#     statistics = get_statistics_of_team(1, db=test_main_database)
#     assert statistics["wins"] == 1
#     assert statistics["losses"] == 2
#     assert statistics["win_ratio"] == 0.33
#     assert statistics["goals_for"] == 6
#     assert statistics["goals_against"] == 7
#     assert statistics["goals_difference"] == -1


# def test_statistics_retrieval_for_team_2(test_main_database):
#     """
#     Tests the CRUD action to retrieve statistics for a single team
#     """
#     statistics = get_statistics_of_team(2, db=test_main_database)
#     assert statistics["wins"] == 2
#     assert statistics["losses"] == 1
#     assert statistics["win_ratio"] == 0.67
#     assert statistics["goals_for"] == 7
#     assert statistics["goals_against"] == 6
#     assert statistics["goals_difference"] == 1


# def test_statistics_retrieval_for_team_3(test_main_database):
#     """
#     Tests the CRUD action to retrieve statistics for a single team
#     """
#     statistics = get_statistics_of_team(3, db=test_main_database)
#     assert statistics["wins"] == 3
#     assert statistics["losses"] == 1
#     assert statistics["win_ratio"] == 0.75
#     assert statistics["goals_for"] == 14
#     assert statistics["goals_against"] == 4
#     assert statistics["goals_difference"] == 10


# def test_statistics_retrieval_for_team_4(test_main_database):
#     """
#     Tests the CRUD action to retrieve statistics for a single team
#     """
#     statistics = get_statistics_of_team(4, db=test_main_database)
#     assert statistics["wins"] == 1
#     assert statistics["losses"] == 3
#     assert statistics["win_ratio"] == 0.25
#     assert statistics["goals_for"] == 4
#     assert statistics["goals_against"] == 14
#     assert statistics["goals_difference"] == -10


# def test_statistics_retrieval_for_all_teams(test_main_database):
#     """
#     Tetst the statistics retrieval for all teams
#     """
#     teams_statistics = get_statistics_dictionary_of_all_teams(db=test_main_database)
#     assert len(teams_statistics.keys()) == 4
#     assert teams_statistics[1]["wins"] == 1
#     assert teams_statistics[2]["win_ratio"] == 0.67


# def test_statistics_retrieval_for_all_players(test_main_database):
#     """
#     Tests the statistics retrieval for all players
#     """

#     team_ids_to_stats = {
#         1: {
#             "wins": 1,
#             "losses": 2,
#             "win_ratio": 0.33,
#             "goals_for": 6,
#             "goals_against": 7,
#             "goals_difference": -1,
#         },
#         2: {
#             "wins": 2,
#             "losses": 1,
#             "win_ratio": 0.66,
#             "goals_for": 7,
#             "goals_against": 6,
#             "goals_difference": 1,
#         },
#         3: {
#             "wins": 3,
#             "losses": 1,
#             "win_ratio": 0.75,
#             "goals_for": 14,
#             "goals_against": 4,
#             "goals_difference": 10,
#         },
#         4: {
#             "wins": 1,
#             "losses": 3,
#             "win_ratio": 0.25,
#             "goals_for": 4,
#             "goals_against": 14,
#             "goals_difference": -10,
#         },
#     }

#     statistics = get_statistics_of_all_players(
#         team_ids_to_stats=team_ids_to_stats, db=test_main_database
#     )
#     assert statistics[0]["name"] == "Player1"
#     assert statistics[0]["wins"] == 4
#     assert statistics[0]["losses"] == 3
#     assert statistics[0]["win_ratio"] == 0.57
#     assert statistics[0]["goals_for"] == 20
#     assert statistics[0]["goals_against"] == 11
#     assert statistics[0]["goals_difference"] == 9

#     assert statistics[1]["name"] == "Player2"
#     assert statistics[1]["wins"] == 2
#     assert statistics[1]["losses"] == 1
#     assert statistics[1]["win_ratio"] == 0.67
#     assert statistics[1]["goals_for"] == 7
#     assert statistics[1]["goals_against"] == 6
#     assert statistics[1]["goals_difference"] == 1

#     assert statistics[2]["name"] == "Player3"
#     assert statistics[2]["wins"] == 2
#     assert statistics[2]["losses"] == 5
#     assert statistics[2]["win_ratio"] == 0.29
#     assert statistics[2]["goals_for"] == 10
#     assert statistics[2]["goals_against"] == 21
#     assert statistics[2]["goals_difference"] == -11

#     assert statistics[3]["name"] == "Player4"
#     assert statistics[3]["wins"] == 2
#     assert statistics[3]["losses"] == 1
#     assert statistics[3]["win_ratio"] == 0.67
#     assert statistics[3]["goals_for"] == 7
#     assert statistics[3]["goals_against"] == 6
#     assert statistics[3]["goals_difference"] == 1
