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

    def test_statistics_retrieval_for_team_1(self, test_statistics_database):
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

    def test_statistics_retrieval_for_team_2(self, test_statistics_database):
        """
        Tests the CRUD action to retrieve statistics for a single team
        """
        statistics = get_statistics_for_team(2, db=test_statistics_database)
        assert statistics["wins"] == 2
        assert statistics["losses"] == 1
        assert statistics["win_ratio"] == 0.67
        assert statistics["goals_for"] == 7
        assert statistics["goals_against"] == 6
        assert statistics["goal_difference"] == 1

    def test_statistics_retrieval_for_team_3(self, test_statistics_database):
        """
        Tests the CRUD action to retrieve statistics for a single team
        """
        statistics = get_statistics_for_team(3, db=test_statistics_database)
        assert statistics["wins"] == 3
        assert statistics["losses"] == 1
        assert statistics["win_ratio"] == 0.75
        assert statistics["goals_for"] == 14
        assert statistics["goals_against"] == 4
        assert statistics["goal_difference"] == 10

    def test_statistics_retrieval_for_team_4(self, test_statistics_database):
        """
        Tests the CRUD action to retrieve statistics for a single team
        """
        statistics = get_statistics_for_team(4, db=test_statistics_database)
        assert statistics["wins"] == 1
        assert statistics["losses"] == 3
        assert statistics["win_ratio"] == 0.25
        assert statistics["goals_for"] == 4
        assert statistics["goals_against"] == 14
        assert statistics["goal_difference"] == -10
