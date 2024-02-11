"""
Test module for Teams routers
"""

from fastapi.testclient import TestClient
from api.main import app


class TestTeamsRouters:
    """
    Class to test the teams routers
    """

    client = None

    @classmethod
    def setup_class(cls):
        """
        Setup method that runs before all tests
        """
        cls.client = TestClient(app)

    def test_successful_team_creation(self, test_main_database):
        """
        Tests router POST /teams
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/teams/",
            json={"name": "Test Name", "first_player_id": 1, "second_player_id": 2},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "Test Name"
        assert "id" in data

    def test_team_creation_throws_400_if_same_player_id(self, test_main_database):
        """
        Tests router POST /teams with first and second player having the same ID
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/teams/",
            json={"name": "Test Name", "first_player_id": 1, "second_player_id": 1},
        )
        assert response.status_code == 400

    def test_team_creation_throws_400_if_first_player_does_not_exist(
        self, test_main_database
    ):
        """
        Tests router POST /teams with first player not existing
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/teams/",
            json={"name": "Test Name", "first_player_id": 999, "second_player_id": 1},
        )
        assert response.status_code == 400

    def test_team_creation_throws_400_if_second_player_does_not_exist(
        self, test_main_database
    ):
        """
        Tests router POST /teams with second player not existing
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/teams/",
            json={"name": "Test Name", "first_player_id": 1, "second_player_id": 999},
        )
        assert response.status_code == 400

    def test_team_listing_returns_all_teams(self, test_main_database):
        """
        Tests router GET /teams
        """
        # pylint: disable=unused-argument
        response = self.client.get(
            "/teams/",
        )
        assert response.status_code == 200
        teams = response.json()
        assert len(teams) == 4
