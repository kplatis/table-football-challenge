"""
Test module for Player CRUD actions
"""

import pytest
from api.exceptions import (
    GameDoesNotExistException,
    SameTeamsGameException,
    TeamDoesNotExistException,
)
from api.games.crud import create_game, retrieve_game, list_games, partial_update_game
from api.games.models import Game
from api.games.schemas import GameCreate, GamePartialUpdate


def test_games_listing_returns_all_games(test_main_database):
    """
    Tests whether all games are returned
    """

    games = list_games(db=test_main_database)
    assert len(games) == 7


def test_games_listing_returns_all_games_with_filters(test_main_database):
    """
    Tests whether all games are returned when applying versus filter
    """

    games = list_games(
        db=test_main_database, first_team_id_versus=1, second_team_id_versus=2
    )
    assert len(games) == 3


def test_create_game_success(test_main_database):
    """
    Tests the CRUD action to create a new game
    """
    game_data = GameCreate(first_team_id=1, second_team_id=2)
    created_game = create_game(db=test_main_database, game=game_data)
    assert isinstance(created_game, Game)


def test_create_game_without_goals_provided_have_0_goals(test_main_database):
    """
    Tests the CRUD action to create a new game
    """
    game_data = GameCreate(first_team_id=1, second_team_id=2)
    created_game = create_game(db=test_main_database, game=game_data)
    assert created_game.first_team_goals == 0
    assert created_game.second_team_goals == 0


def test_game_creation_throws_exception_if_same_team_id(test_main_database):
    """
    Tests whether the game creation throws exception when first and second player have the same ID
    """
    game_data = GameCreate(first_team_id=1, second_team_id=1)
    with pytest.raises(SameTeamsGameException):
        create_game(db=test_main_database, game=game_data)


def test_game_creation_throws_exception_if_first_team_does_not_exist(
    test_main_database,
):
    """
    Tests whether the game creation throws exception when first team does not exist
    """
    game_data = GameCreate(first_team_id=999, second_team_id=2)

    with pytest.raises(TeamDoesNotExistException):
        create_game(db=test_main_database, game=game_data)


def test_game_creation_throws_exception_if_second_team_does_not_exist(
    test_main_database,
):
    """
    Tests whether the game creation throws exception when second team does not exist
    """
    game_data = GameCreate(first_team_id=1, second_team_id=999)

    with pytest.raises(TeamDoesNotExistException):
        create_game(db=test_main_database, game=game_data)


def test_game_patching_successfully_updates_the_game(test_main_database):
    """
    Tests whether a game is correctly updated
    """

    game_data = GamePartialUpdate(first_team_goals=2, second_team_goals=1)
    updated_game = partial_update_game(db=test_main_database, game_id=1, game=game_data)
    assert updated_game.first_team_goals == 2
    assert updated_game.second_team_goals == 1


def test_game_patching_raises_exception_if_game_does_not_exist(test_main_database):
    """
    Tests whether a game patching correctly raises exception if game does not exist
    """

    game_data = GamePartialUpdate(first_team_goals=2, second_team_goals=1)
    with pytest.raises(GameDoesNotExistException):
        partial_update_game(db=test_main_database, game_id=999, game=game_data)


def test_single_game_retrieval_returns_correct_game(test_main_database):
    """
    Tests whether a game retrieval finds the correct game
    """

    game = retrieve_game(db=test_main_database, game_id=1)
    assert game.id == 1


def test_single_game_retrieval_raises_exception_if_not_exist(test_main_database):
    """
    Tests whether a game retrieval correctly raises exception if game does not exist
    """
    with pytest.raises(GameDoesNotExistException):
        retrieve_game(db=test_main_database, game_id=999)
