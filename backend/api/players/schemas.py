"""
Schema declaration for Players module
"""

from typing import List
from pydantic import BaseModel
from api.teams.schemas import Team


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
    first_player_teams: List[Team]
    second_player_teams: List[Team]
