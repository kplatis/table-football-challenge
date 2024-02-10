"""
Router definition for Game module
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_db
from api.exceptions import (
    GameDoesNotExistException,
    SameTeamsGameException,
    TeamDoesNotExistException,
)
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


@router.patch("/{game_id}", tags=["Games"], response_model=schemas.Game)
async def patch_game(
    game_id: int, game: schemas.GamePartialUpdate, db: Session = Depends(get_db)
):
    """
    Defines endpoint to list all games
    """
    try:
        return crud.partial_update_game(db, game_id, game)
    except GameDoesNotExistException as exc:
        raise HTTPException(status_code=404, detail="Game does not exist") from exc


@router.get("/{game_id}", tags=["Games"], response_model=schemas.Game)
async def get_game(game_id: int, db: Session = Depends(get_db)):
    """
    Defines endpoint to retrieve a single game
    """
    try:
        return crud.retrieve_game(db, game_id)
    except GameDoesNotExistException as exc:
        raise HTTPException(status_code=404, detail="Game does not exist") from exc
