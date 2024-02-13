"""
Test module for Player CRUD actions
"""

import pytest
from api.exceptions import (
    PlayerDoesNotExistException,
    SamePlayersTeamException,
    TeamDoesNotExistException,
)
from api.teams.crud import create_team, get_teams, get_team_by_id
from api.teams.models import Team
from api.teams.schemas import TeamCreate


def test_create_team_success(test_main_database):
    """
    Tests the CRUD action to create a new team
    """
    team_data = TeamCreate(name="Test Team", first_player_id=1, second_player_id=2)
    created_team = create_team(db=test_main_database, team=team_data)
    assert isinstance(created_team, Team)


def test_team_creation_throws_exception_if_same_player_id(test_main_database):
    """
    Tests whether the team creation throws exception when first and second player have the same ID
    """
    team_data = TeamCreate(name="Test Team", first_player_id=1, second_player_id=1)
    with pytest.raises(SamePlayersTeamException):
        create_team(db=test_main_database, team=team_data)


def test_team_creation_throws_exception_if_first_player_does_not_exist(
    test_main_database,
):
    """
    Tests whether the team creation throws exception when first player does not exist
    """
    team_data = TeamCreate(name="Test Team", first_player_id=999, second_player_id=1)
    with pytest.raises(PlayerDoesNotExistException):
        create_team(db=test_main_database, team=team_data)


def test_team_creation_throws_exception_if_second_player_does_not_exist(
    test_main_database,
):
    """
    Tests whether the team creation throws exception when second player does not exist
    """
    team_data = TeamCreate(name="Test Team", first_player_id=1, second_player_id=999)
    with pytest.raises(PlayerDoesNotExistException):
        create_team(db=test_main_database, team=team_data)


def test_team_listing_returns_all_teams(test_main_database):
    """
    Tests whether all teams are returned
    """

    teams = get_teams(db=test_main_database)
    assert len(teams) == 5


def test_team_retrieval_by_id_returns_correct_team(test_main_database):
    """
    Tests whether all teams are returned
    """

    team = get_team_by_id(team_id=2, db=test_main_database)
    assert team.id == 2


def test_team_retrieval_by_id_raises_exception_if_team_does_not_exist(
    test_main_database,
):
    """
    Tests whether the CRUD action will raise an exception if team with the given ID does
    not exist in the db
    """

    with pytest.raises(TeamDoesNotExistException):
        get_team_by_id(team_id=999, db=test_main_database)
