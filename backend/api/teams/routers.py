"""
Defines routers for Team module
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from api.dependencies import get_db
from api.teams import crud, schemas


router = APIRouter()


@router.post("", tags=["Teams"], response_model=schemas.Team)
async def create_new_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    """
    Defines endpoint to create a new team
    """
    return crud.create_team(db, team)


@router.get("", tags=["Teams"], response_model=List[schemas.Team])
async def get_all_teams(db: Session = Depends(get_db)):
    """
    Defines endpoint to get all teams
    """
    return crud.get_teams(db)
