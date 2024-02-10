"""
Router definition for Game module
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_db
from api.exceptions import SameTeamsGameException, TeamDoesNotExistException
from api.games import schemas, crud

router = APIRouter()


@router.post("", tags=["Games"], response_model=schemas.Game)
async def create_new_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    """
    Defines endpoint to create a new game
    """
    try:
        return crud.create_game(db, game)
    except TeamDoesNotExistException as exc:
        raise HTTPException(
            status_code=400, detail="First or second team do not exist"
        ) from exc
    except SameTeamsGameException as exc:
        raise HTTPException(
            status_code=400, detail="Cannot create a game using the same teams"
        ) from exc


@router.get("", tags=["Games"], response_model=List[schemas.Game])
async def list_all_games(db: Session = Depends(get_db)):
    """
    Defines endpoint to list all games
    """

    return crud.list_games(db)