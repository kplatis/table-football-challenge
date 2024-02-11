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
