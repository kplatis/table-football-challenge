"""
Unit test module for crud actions
"""

from fastapi.testclient import TestClient
from api.main import app
from api.players.crud import create_player, get_players
from api.players.models import Player
from api.players.schemas import PlayerCreate


def test_create_player(test_main_database, test_client):
    """
    Tests successful player creation
    """
    player = PlayerCreate(name="test")
    created_player = create_player(db=test_main_database, player=player)
    assert isinstance(created_player, Player)


def test_get_players(test_main_database):
    """
    Tests successful listing of players
    """
    players = get_players(db=test_main_database)
    assert len(players) == 5
