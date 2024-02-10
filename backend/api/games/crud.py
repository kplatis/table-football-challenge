"""
CRUD definition for Game module
"""

from sqlalchemy.orm import Session
from api.exceptions import SameTeamsGameException, TeamDoesNotExistException
from api.games import schemas, models as game_models
from api.teams import models as teams_models


def create_game(db: Session, team: schemas.GameCreate):
    """
    CRUD action to create a new team
    """

    # checking if first team exists or not
    first_team = db.get(teams_models.Team, team.first_team_id)
    second_team = db.get(teams_models.Team, team.second_team_id)
    if not first_team or not second_team:
        raise TeamDoesNotExistException
    if first_team.id == second_team.id:
        raise SameTeamsGameException

    # create game object
    db_game = game_models.Game(
        first_team_id=team.first_team_id,
        second_team_id=team.second_team_id,
        first_team_goals=team.first_team_goals,
        second_team_goals=team.second_team_goals,
    )
    # add the object in the db and refresh
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def list_games(db: Session):
    """
    CRUD action to list all games
    """
    return db.query(game_models.Game).all()
