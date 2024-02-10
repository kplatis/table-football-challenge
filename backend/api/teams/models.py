"""
Model declaration for Teams
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base


class Team(Base):
    """
    SQLAlchemy model defining the team model
    """

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    first_player_id = Column(Integer, ForeignKey("users.id"))
    first_player = relationship(
        "api.users.models.User",
        back_populates="first_player_teams",
        foreign_keys=[first_player_id],
    )
    second_player_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    second_player = relationship(
        "api.users.models.User",
        back_populates="second_player_teams",
        foreign_keys=[second_player_id],
    )
