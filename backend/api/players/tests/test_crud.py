"""
Unit test module for crud actions
"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from api.database import Base
from api.main import app
from api.players.crud import create_player, get_players
from api.players.models import Player
from api.players.schemas import PlayerCreate


class TestPlayerCrud:
    """
    Tests the CRUD functions for player
    """

    @classmethod
    def setup_class(cls):
        """
        Setup function run before tests
        """
        sqlalchemy_database_url = "sqlite:///:memory:"
        cls.engine = create_engine(
            sqlalchemy_database_url,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        cls.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=cls.engine
        )
        cls.Base = Base
        cls.Base.metadata.create_all(bind=cls.engine)

        cls.app = app
        cls.client = TestClient(cls.app)
        cls.db = cls.SessionLocal()

    @classmethod
    def teardown_class(cls):
        """
        Teardown function run after tests
        """
        cls.engine.dispose()

    def test_create_player(self):
        """
        Tests successful player creation
        """
        player = PlayerCreate(name="test")
        created_player = create_player(db=self.db, player=player)
        assert isinstance(created_player, Player)

    def test_get_players(self):
        """
        Tests successful listing of players
        """
        players = get_players(db=self.db)
        assert len(players) == 1
