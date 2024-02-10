"""
Schemas definition for Games module
"""

from typing import Optional
from pydantic import BaseModel


class GameBase(BaseModel):
    """
    Base schema definition for Game
    """

    first_team_goals: Optional[int] = None
    second_team_goals: Optional[int] = None


class GameCreate(GameBase):
    """
    Schema definition for game creation
    """

    first_team_id: int
    second_team_id: int


class Game(GameBase):
    """
    Schema definition for game
    """

    id: int
    first_team_id: int
    second_team_id: int


class GamePartialUpdate(GameBase):
    """
    Schema definition for game update
    """

    pass
