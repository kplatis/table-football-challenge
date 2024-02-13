"""
Defines routers for Team module
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_db
from api.exceptions import (
    PlayerDoesNotExistException,
    SamePlayersTeamException,
    TeamDoesNotExistException,
)
from api.teams import crud, schemas


router = APIRouter()


@router.post("", tags=["Teams"], response_model=schemas.Team)
async def create_new_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    """
    Defines endpoint to create a new team
    """
    try:
        return crud.create_team(db, team)
    except PlayerDoesNotExistException as exc:
        raise HTTPException(
            status_code=400, detail="First or second player do not exist"
        ) from exc
    except SamePlayersTeamException as exc:
        raise HTTPException(
            status_code=400,
            detail="Team must have either one player or two different players",
        ) from exc


@router.get("", tags=["Teams"], response_model=List[schemas.Team])
async def get_all_teams(db: Session = Depends(get_db)):
    """
    Defines endpoint to get all teams
    """
    return crud.get_teams(db)


@router.get("/{team_id}", tags=["Teams"], response_model=schemas.Team)
async def get_team_by_id(team_id: int, db: Session = Depends(get_db)):
    """
    Defines endpoint to get all teams
    """
    try:
        return crud.get_team_by_id(team_id, db)
    except TeamDoesNotExistException as exc:
        raise HTTPException(status_code=404, detail="Team does not exist") from exc
