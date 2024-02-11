"""
Defines the common fixtures for unit tests
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base
from api.dependencies import get_db
from api.main import app
from api.players.crud import create_player
from api.players.models import Player
from api.teams.crud import create_team
from api.teams.models import Team

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", name="test_app")
def test_application():
    """
    Setup a test app
    """
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield app
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


@pytest.fixture(scope="session")
def test_main_database(test_app):
    """
    Setup a test main database with players and teams
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
        teams_data = [
            {"name": "team1", "first_player_id": 1},
            {"name": "team2", "first_player_id": 2},
        ]
        for team_data in teams_data:
            create_team(db, Team(**team_data))

        db.commit()
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)
