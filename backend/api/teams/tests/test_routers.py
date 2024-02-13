"""
Test module for Teams routers
"""


def test_successful_team_creation(test_main_database, test_client):
    """
    Tests router POST /teams
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/teams/",
        json={"name": "Test Name", "first_player_id": 1, "second_player_id": 2},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test Name"
    assert "id" in data


def test_team_creation_throws_400_if_same_player_id(test_main_database, test_client):
    """
    Tests router POST /teams with first and second player having the same ID
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/teams/",
        json={"name": "Test Name", "first_player_id": 1, "second_player_id": 1},
    )
    assert response.status_code == 400


def test_team_creation_throws_400_if_first_player_does_not_exist(
    test_main_database, test_client
):
    """
    Tests router POST /teams with first player not existing
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/teams/",
        json={"name": "Test Name", "first_player_id": 999, "second_player_id": 1},
    )
    assert response.status_code == 400


def test_team_creation_throws_400_if_second_player_does_not_exist(
    test_main_database, test_client
):
    """
    Tests router POST /teams with second player not existing
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/teams/",
        json={"name": "Test Name", "first_player_id": 1, "second_player_id": 999},
    )
    assert response.status_code == 400


def test_team_listing_returns_all_teams(test_main_database, test_client):
    """
    Tests router GET /teams
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/teams/",
    )
    assert response.status_code == 200
    teams = response.json()
    assert len(teams) == 5


def test_team_retrieval_by_id_returns_correct_team(test_main_database, test_client):
    """
    Tests router GET /teams/<ID>
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/teams/2",
    )
    assert response.status_code == 200
    team = response.json()
    assert team["id"] == 2


def test_team_retrieval_by_id_returns_404_if_test_does_exist(
    test_main_database, test_client
):
    """
    Tests router GET /teams/<ID>
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/teams/999",
    )
    assert response.status_code == 404
