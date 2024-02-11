"""
Test module for Statistics routers
"""

from fastapi.testclient import TestClient
from api.main import app


class TestStatisticsRouters:
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

    def test_statistics_overview_returns_both_players_and_teams(
        self, test_statistics_database
    ):
        """
        Tests router POST /statistics/overview
        """
        # pylint: disable=unused-argument
        response = self.client.get("/statistics/overview")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 8
