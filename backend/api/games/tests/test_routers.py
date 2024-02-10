"""
Test module for Games routers
"""

from fastapi.testclient import TestClient
from api.main import app


class TestGamesRouters:
    """
    Class to test the games routers
    """

    client = None

    @classmethod
    def setup_class(cls):
        """
        Setup method that runs before all tests
        """
        cls.client = TestClient(app)

    def test_successful_game_creation(self, test_database):
        """
        Tests router POST /games
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/games",
            json={"first_team_id": 1, "second_team_id": 2},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert "id" in data

    def test_game_creation_throws_400_if_same_team_id(self, test_database):
        """
        Tests router POST /games with first and second team having the same ID
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/games",
            json={"first_team_id": 1, "second_team_id": 1},
        )
        assert response.status_code == 400

    def test_game_creation_throws_400_if_first_team_does_not_exist(self, test_database):
        """
        Tests router POST /games with first team not existing
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/games",
            json={"first_team_id": 999, "second_team_id": 1},
        )
        assert response.status_code == 400

    def test_game_creation_throws_400_if_second_team_does_not_exist(
        self, test_database
    ):
        """
        Tests router POST /games with second team not existing
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/games",
            json={"first_team_id": 1, "second_team_id": 999},
        )
        assert response.status_code == 400

    def test_game_listing_returns_all_games(self, test_database):
        """
        Tests router GET /games
        """
        # pylint: disable=unused-argument
        response = self.client.get(
            "/games",
        )
        assert response.status_code == 200
        teams = response.json()
        assert len(teams) == 3

    def test_game_partial_update_returns_200_if_correct(self, test_database):
        """
        Tests router GET /games
        """
        # pylint: disable=unused-argument
        response = self.client.patch(
            "/games/1",
            json={"first_team_goals": 2, "second_team_goals": 1},
        )
        assert response.status_code == 200
        game = response.json()
        assert game["first_team_goals"] == 2
        assert game["second_team_goals"] == 1

    def test_game_partial_update_returns_404_if_game_does_not_exist(
        self, test_database
    ):
        """
        Tests router GET /games
        """
        # pylint: disable=unused-argument
        response = self.client.patch(
            "/games/999",
            json={"first_team_goals": 2, "second_team_goals": 1},
        )
        assert response.status_code == 404
