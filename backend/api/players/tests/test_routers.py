"""
Test module for Player routers
"""

from fastapi.testclient import TestClient
from api.main import app


def test_player_creation(test_main_database, test_client):
    """
    Tests router POST /players
    """
    # pylint: disable=unused-argument
    response = test_client.post(
        "/players/",
        json={"name": "Test Name"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test Name"
    assert "id" in data


def test_players_listing(test_main_database, test_client):
    """
    Tests router GET /players
    """
    # pylint: disable=unused-argument
    response = test_client.get("/players/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) == 5
