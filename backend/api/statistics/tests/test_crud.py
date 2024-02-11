"""
Define unit tests for CRUD actions of statistics
"""

from fastapi.testclient import TestClient
from api.main import app
from api.statistics.crud import get_statistics_for_team


class TestGameCrud:
    """
    Class to test the crud actions for games
    """

    client = None

    @classmethod
    def setup_class(cls):
        """
        Setup method that runs before all tests
        """
        cls.client = TestClient(app)

    def test_statistics_retrieval_for_team(self, test_statistics_database):
        """
        Tests the CRUD action to retrieve statistics for a single team
        """
        statistics = get_statistics_for_team(1, db=test_statistics_database)
        assert statistics["wins"] == 1
        assert statistics["losses"] == 2
        assert statistics["win_ratio"] == 0.33
        assert statistics["goals_for"] == 6
        assert statistics["goals_against"] == 7
        assert statistics["goal_difference"] == -1
