"""
Schema declaration for Teams module
"""

from typing import Optional
from pydantic import BaseModel


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
    second_player_id: Optional[int]

    class Config:
        """
        Configuration of schema
        """

        orm_mode = True
