"""
Defines the common fixtures for unit tests
"""

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base
from api.dependencies import get_db
from api.main import app
from api.players.crud import create_player
from api.players.models import Player

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


@pytest.fixture(scope="session")
def test_client(test_app):
    """
    Setup a test client
    """
    # pylint: disable=unused-argument
    with TestClient(test_application) as client:
        yield client


@pytest.fixture(scope="session")
def test_database(test_app):
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
