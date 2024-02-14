"""
Router declaration for Statistics module
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query
from api.dependencies import get_db
from api.games.crud import list_games
from api.statistics.calculator import calculate_stats_for_teams_and_players

from api.statistics.schemas import StatisticsByTeamOrPlayer
from api.validators import validate_versus_team_ids


router = APIRouter()


@router.get(
    "/overview", tags=["Statistics"], response_model=List[StatisticsByTeamOrPlayer]
)
async def get_statistics_overview_for_teams_and_players(
    category: str = Query(
        None, description="Category of the item", pattern="^(players|teams|all)$"
    ),
    versus_team_ids: Optional[List[int]] = Query(None, description="List of team IDs"),
    db: Session = Depends(get_db),
):
    """
    Endpoint to retrieve statistics overview for teams and players
    """
    # validates the team_id_versus parameters
    first_team_id_versus, second_team_id_versus = validate_versus_team_ids(
        versus_team_ids
    )

    games = list_games(
        db=db,
        first_team_id_versus=first_team_id_versus,
        second_team_id_versus=second_team_id_versus,
    )
    teams, players = calculate_stats_for_teams_and_players(games)
    if category == "players":
        response = list(players.values())
    elif category == "teams":
        response = list(teams.values())
    else:
        response = list(teams.values()) + list(players.values())
    return [StatisticsByTeamOrPlayer(**response) for response in response]
