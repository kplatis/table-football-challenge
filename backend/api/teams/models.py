"""
Model declaration for Teams
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base


class User(Base):
    """
    SQLAlchemy model defining the user model
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)


class Team(Base):
    """
    SQLAlchemy model defining the team model
    """

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    first_player_id = Column(Integer, ForeignKey("users.id"))
    first_player = relationship("User", back_populates="teams")
    second_player_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    second_player = relationship("User", back_populates="teams")
