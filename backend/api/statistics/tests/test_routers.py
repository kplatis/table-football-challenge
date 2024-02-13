"""
Test module for Statistics routers
"""


def test_statistics_overview_returns_both_players_and_teams(
    test_main_database, test_client
):
    """
    Tests router POST /statistics/overview
    """
    # pylint: disable=unused-argument
    response = test_client.get("/statistics/overview")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 8


def test_statistics_overview_returns_only_players_if_players_query_parameter(
    test_main_database, test_client
):
    """
    Tests router POST /statistics/overview?category=players
    """
    # pylint: disable=unused-argument
    response = test_client.get("/statistics/overview?category=players")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 4


def test_statistics_overview_returns_only_players_if_teams_query_parameter(
    test_main_database, test_client
):
    """
    Tests router POST /statistics/overview?category=teams
    """
    # pylint: disable=unused-argument
    response = test_client.get("/statistics/overview?category=teams")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 4
