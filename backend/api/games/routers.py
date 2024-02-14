"""
Router definition for Game module
"""

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from api.calculator import calculate_stats_for_teams_and_players
from api.dependencies import get_db
from api.exceptions import (
    GameDoesNotExistException,
    SameTeamsGameException,
    TeamDoesNotExistException,
)
from api.games import schemas as games_schemas, crud
from api.games.converter import convert_game_model_to_schema

router = APIRouter()


@router.post("", tags=["Games"], response_model=games_schemas.Game)
async def create_new_game(
    game: games_schemas.GameCreate, db: Session = Depends(get_db)
):
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


@router.get("", tags=["Games"], response_model=games_schemas.GameListResponse)
async def list_all_games(
    with_team_stats: bool = False,
    with_player_stats: bool = False,
    db: Session = Depends(get_db),
):
    """
    Defines endpoint to list all games
    """
    games = crud.list_games(db)
    if with_team_stats or with_player_stats:
        teams, players = calculate_stats_for_teams_and_players(games=games)
    return games_schemas.GameListResponse(
        games=[convert_game_model_to_schema(game) for game in games],
        team_stats=list(teams.values()) if with_team_stats else None,
        player_stats=list(players.values()) if with_player_stats else None,
    )


@router.patch("/{game_id}", tags=["Games"], response_model=games_schemas.Game)
async def patch_game(
    game_id: int, game: games_schemas.GamePartialUpdate, db: Session = Depends(get_db)
):
    """
    Defines endpoint to list all games
    """
    try:
        return crud.partial_update_game(db, game_id, game)
    except GameDoesNotExistException as exc:
        raise HTTPException(status_code=404, detail="Game does not exist") from exc


@router.get("/{game_id}", tags=["Games"], response_model=games_schemas.Game)
async def get_game(game_id: int, db: Session = Depends(get_db)):
    """
    Defines endpoint to retrieve a single game
    """
    try:
        return crud.retrieve_game(db, game_id)
    except GameDoesNotExistException as exc:
        raise HTTPException(status_code=404, detail="Game does not exist") from exc
