"""
CRUD definitions for Team module
"""

from sqlalchemy.orm import Session
from api.exceptions import (
    PlayerDoesNotExistException,
    SamePlayersTeamException,
    TeamDoesNotExistException
)
from api.teams import models as teams_models, schemas as teams_schemas
from api.players import models as players_models


def create_team(db: Session, team: teams_schemas.TeamCreate):
    """
    CRUD action to create a new team
    """

    # checking if first player exists or not
    first_player = db.get(players_models.Player, team.first_player_id)
    if not first_player:
        raise PlayerDoesNotExistException
    # checking if second player exists or not
    if team.second_player_id is not None:
        second_player = db.get(players_models.Player, team.second_player_id)
        if not second_player:
            raise PlayerDoesNotExistException
    # checking if first and second player are the same
    if team.second_player_id and team.first_player_id == team.second_player_id:
        raise SamePlayersTeamException
    # create team object
    db_team = teams_models.Team(
        name=team.name,
        first_player_id=team.first_player_id,
        second_player_id=team.second_player_id if team.second_player_id else None,
    )
    # add the object in the db and refresh
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def get_teams(db: Session):
    """
    CRUD action to read all teams
    """
    return db.query(teams_models.Team).all()


def get_team_by_id(team_id: int, db: Session):
    """
    CRUD action to retrieve team using its ID
    """
    team = db.get(teams_models.Team, team_id)
    if team is None:
        raise TeamDoesNotExistException
    return team
