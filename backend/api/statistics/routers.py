"""
Router declaration for Statistics module
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query
from api.dependencies import get_db
from api.statistics.crud import (
    get_statistics_dictionary_of_all_teams,
    get_statistics_of_all_players,
)
from api.statistics.schemas import StatisticsByTeamOrPlayer


router = APIRouter()


@router.get(
    "/overview", tags=["Statistics"], response_model=List[StatisticsByTeamOrPlayer]
)
async def get_statistics_overview_for_teams_and_players(
    category: str = Query(
        None, description="Category of the item", pattern="^(players|teams)$"
    ),
    db: Session = Depends(get_db),
):
    """
    Endpoint to retrieve statistics overview for teams and players
    """
    # retrieve the statistics dictionary of all teams
    team_ids_to_statistics = get_statistics_dictionary_of_all_teams(db)
    # retrieve the statistics list of all players
    player_statistics = get_statistics_of_all_players(
        team_ids_to_stats=team_ids_to_statistics, db=db
    )
    if category == "players":
        response = player_statistics
    elif category == "teams":
        response = list(team_ids_to_statistics.values())
    else:
        response = list(team_ids_to_statistics.values()) + player_statistics
    return [StatisticsByTeamOrPlayer(**response) for response in response]
