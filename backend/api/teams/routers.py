"""
Defines routers for Team module
"""

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
