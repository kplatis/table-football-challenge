"""
Test module for Player CRUD actions
"""

from fastapi.testclient import TestClient
import pytest
from api.exceptions import (
    SameTeamsGameException,
    TeamDoesNotExistException,
)
from api.games.crud import create_game, list_games
from api.games.models import Game
from api.games.schemas import GameCreate
from api.main import app


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

    def test_create_game_success(self, test_database):
        """
        Tests the CRUD action to create a new game
        """
        game_data = GameCreate(first_team_id=1, second_team_id=2)
        created_game = create_game(db=test_database, game=game_data)
        assert isinstance(created_game, Game)

    def test_create_game_without_goals_provided_have_0_goals(self, test_database):
        """
        Tests the CRUD action to create a new game
        """
        game_data = GameCreate(first_team_id=1, second_team_id=2)
        created_game = create_game(db=test_database, game=game_data)
        assert created_game.first_team_goals == 0
        assert created_game.second_team_goals == 0

    def test_game_creation_throws_exception_if_same_team_id(self, test_database):
        """
        Tests whether the game creation throws exception when first and second player have the same ID
        """
        game_data = GameCreate(first_team_id=1, second_team_id=1)
        with pytest.raises(SameTeamsGameException):
            create_game(db=test_database, game=game_data)

    def test_game_creation_throws_exception_if_first_team_does_not_exist(
        self, test_database
    ):
        """
        Tests whether the game creation throws exception when first team does not exist
        """
        game_data = GameCreate(first_team_id=999, second_team_id=2)

        with pytest.raises(TeamDoesNotExistException):
            create_game(db=test_database, game=game_data)

    def test_game_creation_throws_exception_if_second_team_does_not_exist(
        self, test_database
    ):
        """
        Tests whether the game creation throws exception when second team does not exist
        """
        game_data = GameCreate(first_team_id=1, second_team_id=999)

        with pytest.raises(TeamDoesNotExistException):
            create_game(db=test_database, game=game_data)

    def test_games_listing_returns_all_games(self, test_database):
        """
        Tests whether all games are returned
        """

        games = list_games(db=test_database)
        assert len(games) == 2