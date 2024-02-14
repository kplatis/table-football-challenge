"""
Test module for Games routers
"""


def test_game_listing_returns_all_games(test_main_database, test_client):
    """
    Tests router GET /games
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/games",
    )
    assert response.status_code == 200
    teams = response.json()
    assert len(teams) == 7


def test_game_listing_returns_all_filtered_versus(test_main_database, test_client):
    """
    Tests router GET /games
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/games?versus_team_ids=3&versus_team_ids=4",
    )
    assert response.status_code == 200
    teams = response.json()
    assert len(teams) == 4


def test_game_listing_returns_correct_filtered_versus_if_two_teams_did_not_play(
    test_main_database, test_client
):
    """
    Tests router GET /games
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/games?versus_team_ids=1&versus_team_ids=4",
    )
    assert response.status_code == 200
    teams = response.json()
    assert len(teams) == 0


def test_game_listing_returns_400_if_only_one_team_provided_in_versus(
    test_main_database, test_client
):
    """
    Tests router GET /games
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/games?versus_team_ids=1",
    )
    assert response.status_code == 400


def test_successful_game_creation(test_main_database, test_client):
    """
    Tests router POST /games
    """
    # pylint: disable=unused-argument

    response = test_client.post(
        "/games",
        json={"first_team_id": 1, "second_team_id": 2},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data


def test_game_creation_throws_400_if_same_team_id(test_main_database, test_client):
    """
    Tests router POST /games with first and second team having the same ID
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/games",
        json={"first_team_id": 1, "second_team_id": 1},
    )
    assert response.status_code == 400


def test_game_creation_throws_400_if_first_team_does_not_exist(
    test_main_database, test_client
):
    """
    Tests router POST /games with first team not existing
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/games",
        json={"first_team_id": 999, "second_team_id": 1},
    )
    assert response.status_code == 400


def test_game_creation_throws_400_if_second_team_does_not_exist(
    test_main_database, test_client
):
    """
    Tests router POST /games with second team not existing
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/games",
        json={"first_team_id": 1, "second_team_id": 999},
    )
    assert response.status_code == 400


def test_game_partial_update_returns_200_if_correct(test_main_database, test_client):
    """
    Tests router GET /games
    """
    # pylint: disable=unused-argument
    response = test_client.patch(
        "/games/1",
        json={"first_team_goals": 2, "second_team_goals": 1},
    )
    assert response.status_code == 200
    game = response.json()
    assert game["first_team_goals"] == 2
    assert game["second_team_goals"] == 1


def test_game_partial_update_returns_404_if_game_does_not_exist(
    test_main_database, test_client
):
    """
    Tests router GET /games
    """
    # pylint: disable=unused-argument
    response = test_client.patch(
        "/games/999",
        json={"first_team_goals": 2, "second_team_goals": 1},
    )
    assert response.status_code == 404


def test_game_retrieval_returns_game(test_main_database, test_client):
    """
    Tests router GET /games/<ID>
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/games/1",
    )
    assert response.status_code == 200
    team = response.json()
    assert team["id"] == 1


def test_game_retrieval_returns_404_if_game_does_not_exist(
    test_main_database, test_client
):
    """
    Tests router GET /games/<ID> throws 404
    """
    # pylint: disable=unused-argument
    response = test_client.get(
        "/games/999",
    )
    assert response.status_code == 404
