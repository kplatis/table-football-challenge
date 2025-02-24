"""
CRUD definition for Game module
"""

from sqlalchemy.orm import Session
from api.exceptions import (
    GameDoesNotExistException,
    SameTeamsGameException,
    TeamDoesNotExistException,
)
from api.games import schemas, models as game_models
from api.teams import models as teams_models


def create_game(db: Session, game: schemas.GameCreate):
    """
    CRUD action to create a new team
    """

    # checking if first team exists or not
    first_team = db.get(teams_models.Team, game.first_team_id)
    second_team = db.get(teams_models.Team, game.second_team_id)
    if not first_team or not second_team:
        raise TeamDoesNotExistException
    if first_team.id == second_team.id:
        raise SameTeamsGameException

    # create game object
    db_game = game_models.Game(
        first_team_id=game.first_team_id,
        second_team_id=game.second_team_id,
        first_team_goals=game.first_team_goals,
        second_team_goals=game.second_team_goals,
    )
    # add the object in the db and refresh
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def list_games(
    db: Session, first_team_id_versus: int = None, second_team_id_versus: int = None
):
    """
    CRUD action to list all games
    """
    # if versus teams are provided
    if first_team_id_versus is not None and second_team_id_versus is not None:
        return (
            db.query(game_models.Game)
            .filter(
                (
                    (game_models.Game.first_team_id == first_team_id_versus)
                    & (game_models.Game.second_team_id == second_team_id_versus)
                )
                | (
                    (game_models.Game.first_team_id == second_team_id_versus)
                    & (game_models.Game.second_team_id == first_team_id_versus)
                )
            )
            .all()
        )

    return db.query(game_models.Game).all()


def partial_update_game(db: Session, game_id: int, game: schemas.GamePartialUpdate):
    """
    CRUD action to patch a game object
    """
    db_game = db.get(game_models.Game, game_id)
    if not db_game:
        raise GameDoesNotExistException
    if game.first_team_goals:
        db_game.first_team_goals = game.first_team_goals
    if game.second_team_goals:
        db_game.second_team_goals = game.second_team_goals

    # Commit changes to the database
    db.commit()
    # Refresh the game object
    db.refresh(db_game)
    return db_game


def retrieve_game(db: Session, game_id: int):
    """
    CRUD action to get single game
    """
    game = db.get(game_models.Game, game_id)
    if not game:
        raise GameDoesNotExistException
    return game
