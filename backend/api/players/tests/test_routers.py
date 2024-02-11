"""
Test module for Player routers
"""

from fastapi.testclient import TestClient
from api.main import app


class TestPlayerRouters:
    """
    Class to test the player routers
    """

    client = None

    @classmethod
    def setup_class(cls):
        """
        Setup method that runs before all tests
        """
        cls.client = TestClient(app)

    def test_player_creation(self, test_main_database):
        """
        Tests router POST /players
        """
        # pylint: disable=unused-argument
        response = self.client.post(
            "/players/",
            json={"name": "Test Name"},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "Test Name"
        assert "id" in data

    def test_players_listing(self, test_main_database):
        """
        Tests router GET /players
        """
        # pylint: disable=unused-argument
        response = self.client.get("/players/")
        assert response.status_code == 200, response.text
        data = response.json()
        assert len(data) == 6
