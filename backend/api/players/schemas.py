"""
Schema declaration for Players module
"""

from pydantic import BaseModel


class PlayerBase(BaseModel):
    """
    Base schema declaration for Player
    """

    name: str


class PlayerCreate(PlayerBase):
    """
    Schema declaration for creation of Player
    """

    pass


class Player(PlayerBase):
    """
    Schema declaration for Player
    """

    id: int
