"""
Model declaration for users module
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from api.database import Base
from api.teams.models import Team


class User(Base):
    """
    SQLAlchemy model defining the user model
    """

    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    first_player_teams = relationship(
        "api.teams.models.Team",
        back_populates="first_player",
        foreign_keys=[Team.first_player_id],
    )
    second_player_teams = relationship(
        "api.teams.models.Team",
        back_populates="second_player",
        foreign_keys=[Team.second_player_id],
    )
