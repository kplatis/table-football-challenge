"""
Test module for Player routers
"""

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base
from api.dependencies import get_db
from api.exceptions import PlayerDoesNotExistException, SamePlayersTeamException
from api.main import app
from api.players.crud import create_player
from api.players.models import Player
from api.teams.crud import create_team, get_teams
from api.teams.models import Team
from api.teams.schemas import TeamCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="class", name="test_application")
def test_app():
    """
    Setup a test app
    """
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="class")
def test_client(test_application):
    """
    Setup a test client
    """
    # pylint: disable=unused-argument
    with TestClient(test_app) as client:
        yield client


@pytest.fixture(scope="class", name="test_database")
def test_db(test_application):
    """
    Setup a test database with players
    """
    # pylint: disable=unused-argument
    with TestingSessionLocal() as db:
        players_data = [
            {"name": "Player 1"},
            {"name": "Player 2"},
            {"name": "Player 3"},
            {"name": "Player 4"},
        ]
        for player_data in players_data:
            create_player(db, Player(**player_data))
        db.commit()
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    """
    Mocks the default database
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


class TestTeamCrud:
    """
    Class to test the crud actions for teams
    """

    client = None

    @classmethod
    def setup_class(cls):
        """
        Setup method that runs before all tests
        """
        cls.client = TestClient(app)

    def test_create_team_success(self, test_database):
        """
        Tests the CRUD action to create a new team
        """
        team_data = TeamCreate(name="Test Team", first_player_id=1, second_player_id=2)
        created_team = create_team(db=test_database, team=team_data)
        assert isinstance(created_team, Team)

    def test_team_creation_throws_exception_if_same_player_id(self, test_database):
        """
        Tests whether the team creation throws exception when first and second player have the same ID
        """
        team_data = TeamCreate(name="Test Team", first_player_id=1, second_player_id=1)
        with pytest.raises(SamePlayersTeamException):
            create_team(db=test_database, team=team_data)

    def test_team_creation_throws_exception_if_first_player_does_not_exist(
        self, test_database
    ):
        """
        Tests whether the team creation throws exception when first player does not exist
        """
        team_data = TeamCreate(
            name="Test Team", first_player_id=999, second_player_id=1
        )
        with pytest.raises(PlayerDoesNotExistException):
            create_team(db=test_database, team=team_data)

    def test_team_creation_throws_exception_if_second_player_does_not_exist(
        self, test_database
    ):
        """
        Tests whether the team creation throws exception when second player does not exist
        """
        team_data = TeamCreate(
            name="Test Team", first_player_id=1, second_player_id=999
        )
        with pytest.raises(PlayerDoesNotExistException):
            create_team(db=test_database, team=team_data)

    def test_team_listing_returns_all_teams(self, test_database):
        """
        Tests whether all teams are returned
        """

        teams = get_teams(db=test_database)
        assert len(teams) == 1
