"""
Test module for Player routers
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


@pytest.fixture(scope="class")
def test_app():
    """
    Setup a test app
    """
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="class")
def test_client(test_app):
    """
    Setup a test client
    """
    with TestClient(test_app) as client:
        yield client


@pytest.fixture(scope="class")
def test_db(test_app):
    """
    Setup a test database with players
    """
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


class TestPlayerRouters:
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

    def test_player_creation(self, test_db):
        """
        Tests router POST /players
        """
        response = self.client.post(
            "/players/",
            json={"name": "Test Name"},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["name"] == "Test Name"
        assert "id" in data

    def test_players_listing(self, test_db):
        """
        Tests router GET /players
        """
        response = self.client.get("/players/")
        assert response.status_code == 200, response.text
        data = response.json()
        assert len(data) == 5
