"""
Defines the common fixtures for unit tests
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base
from api.dependencies import get_db
from api.games.crud import create_game
from api.games.models import Game
from api.main import app
from api.players.crud import create_player
from api.players.models import Player
from api.teams.crud import create_team
from api.teams.models import Team

SQLALCHEMY_DATABASE_URL = "sqlite:///./statistics_database.db"

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
def test_statistics_database(test_app):
    """
    Setup a test main database with players, teams and games for the needs of statistics tests
    """
    # pylint: disable=unused-argument
    with TestingSessionLocal() as db:
        players_data = [
            {"name": "Player1"},
            {"name": "Player2"},
            {"name": "Player3"},
            {"name": "Player4"},
        ]
        for player_data in players_data:
            create_player(db, Player(**player_data))
        teams_data = [
            {"name": "team1", "first_player_id": 1, "second_player_id": 3},
            {"name": "team2", "first_player_id": 2, "second_player_id": 4},
            {"name": "team3", "first_player_id": 1},
            {"name": "team4", "first_player_id": 3},
        ]
        for team_data in teams_data:
            create_team(db, Team(**team_data))
        games_data = [
            {
                "first_team_id": 1,
                "second_team_id": 2,
                "first_team_goals": 2,
                "second_team_goals": 1,
            },
            {
                "first_team_id": 1,
                "second_team_id": 2,
                "first_team_goals": 3,
                "second_team_goals": 4,
            },
            {
                "first_team_id": 1,
                "second_team_id": 2,
                "first_team_goals": 1,
                "second_team_goals": 2,
            },
            {
                "first_team_id": 3,
                "second_team_id": 4,
                "first_team_goals": 6,
                "second_team_goals": 0,
            },
            {
                "first_team_id": 3,
                "second_team_id": 4,
                "first_team_goals": 1,
                "second_team_goals": 2,
            },
            {
                "first_team_id": 3,
                "second_team_id": 4,
                "first_team_goals": 3,
                "second_team_goals": 1,
            },
            {
                "first_team_id": 3,
                "second_team_id": 4,
                "first_team_goals": 4,
                "second_team_goals": 1,
            },
        ]
        for game_data in games_data:
            create_game(db, Game(**game_data))

        db.commit()
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)
