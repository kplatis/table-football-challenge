"""
Unit test module for routers
"""

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
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


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)

    # Seed the database with 4 players
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


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_player_creation(test_db):
    """
    Tests router POST /players
    """
    response = client.post(
        "/players/",
        json={"name": "Test Name"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test Name"
    assert "id" in data


def test_players_listing(test_db):
    """
    Tests router GET /players
    """
    response = client.get(
        "/players/",
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) == 4
