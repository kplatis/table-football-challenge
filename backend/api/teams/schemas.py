"""
Schema declaration for Teams module
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class TeamBase(BaseModel):
    """
    Schema declaration for team base
    """

    name: str


class TeamCreate(TeamBase):
    """
    Schema declaration for team creation
    """

    first_player_id: int
    second_player_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)


class Team(TeamBase):
    """
    Schema declaration for team creation
    """

    id: int
    first_player_id: int
    second_player_id: Optional[int]
    model_config = ConfigDict(from_attributes=True)
