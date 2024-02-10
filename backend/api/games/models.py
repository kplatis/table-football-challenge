"""
Model declaration for Games
"""

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from api.database import Base


class Game(Base):
    """
    SQLAlchemy model defining the Game model
    """

    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    first_team_id = Column(Integer, ForeignKey("teams.id"))
    first_team = relationship(
        "api.teams.models.Team",
        back_populates="first_team_games",
        foreign_keys=[first_team_id],
    )
    first_team_goals = Column(Integer, default=0)
    second_team_id = Column(Integer, ForeignKey("teams.id"))
    second_team = relationship(
        "api.teams.models.Team",
        back_populates="second_team_games",
        foreign_keys=[second_team_id],
    )
    second_team_goals = Column(Integer, default=0)
