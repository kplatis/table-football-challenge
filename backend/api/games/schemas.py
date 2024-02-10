"""
Schemas definition for Games module
"""

from pydantic import BaseModel


class GameBase(BaseModel):
    """
    Base schema definition for Game
    """

    first_team_id: int
    second_team_id: int


class GameCreate(GameBase):
    """
    Schema definition for game creation
    """

    pass


class Game(GameBase):
    """
    Schema definition for game
    """

    id: int
