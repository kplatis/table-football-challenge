"""
Router definition for Game module
"""

from typing import List
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
from api.teams import schemas as teams_schemas
from api.players import schemas as players_schemas


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
        games=[
            games_schemas.Game.model_validate(
                {
                    **game.__dict__,
                    "first_team": teams_schemas.Team.model_validate(
                        {
                            **game.first_team.__dict__,
                            "first_player": players_schemas.Player.model_validate(
                                game.first_team.first_player.__dict__
                            ),
                            "second_player": (
                                players_schemas.Player.model_validate(
                                    game.first_team.second_player.__dict__
                                )
                                if game.first_team.second_player
                                else None
                            ),
                        }
                    ),
                    "second_team": teams_schemas.Team.model_validate(
                        {
                            **game.second_team.__dict__,
                            "first_player": players_schemas.Player.model_validate(
                                game.second_team.first_player.__dict__
                            ),
                            "second_player": (
                                players_schemas.Player.model_validate(
                                    game.second_team.second_player.__dict__
                                )
                                if game.second_team.second_player
                                else None
                            ),
                        }
                    ),
                }
            )
            for game in games
        ],
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
