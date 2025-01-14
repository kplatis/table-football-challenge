"""
Schemas definition for Games module
"""

from typing import Optional
from pydantic import BaseModel
from api.teams.schemas import Team


class GameBase(BaseModel):
    """
    Base schema definition for Game
    """

    first_team_goals: Optional[int] = 0
    second_team_goals: Optional[int] = 0


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
    first_team: Team
    second_team: Team


class GamePartialUpdate(GameBase):
    """
    Schema definition for game update
    """

    pass
