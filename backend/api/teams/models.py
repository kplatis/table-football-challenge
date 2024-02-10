"""
Model declaration for Teams
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base
from api.games.models import Game


class Team(Base):
    """
    SQLAlchemy model defining the team model
    """

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    first_player_id = Column(Integer, ForeignKey("players.id"))
    first_player = relationship(
        "api.players.models.Player",
        back_populates="first_player_teams",
        foreign_keys=[first_player_id],
    )
    second_player_id = Column(Integer, ForeignKey("players.id"), nullable=True)
    second_player = relationship(
        "api.players.models.Player",
        back_populates="second_player_teams",
        foreign_keys=[second_player_id],
    )
    first_team_games = relationship(
        "api.games.models.Game",
        back_populates="first_team",
        foreign_keys=[Game.first_team_id],
    )
    second_team_games = relationship(
        "api.games.models.Game",
        back_populates="second_team",
        foreign_keys=[Game.second_team_id],
    )
