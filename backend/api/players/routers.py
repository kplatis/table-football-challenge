"""
Router declaration for Player module
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from api.dependencies import get_db
from api.players import crud, schemas


router = APIRouter()


@router.post("", tags=["Players"], response_model=schemas.Player)
async def create_new_player(
    player: schemas.PlayerCreate, db: Session = Depends(get_db)
):
    """
    Endpoint to create new player
    """
    return crud.create_player(db=db, player=player)


@router.get("", tags=["Players"], response_model=List[schemas.Player])
async def get_all_players(db: Session = Depends(get_db)):
    """
    Endpoint to get players
    """
    return crud.get_players(db)
