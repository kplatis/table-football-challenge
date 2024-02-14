"""
Schema definition for statistics module
"""

from pydantic import BaseModel


class StatisticsByTeamOrPlayer(BaseModel):
    """
    Schema defining statistics by team or player
    """

    name: str
    wins: int
    losses: int
    win_ratio: float
    goals_for: int
    goals_against: int
    goals_difference: int