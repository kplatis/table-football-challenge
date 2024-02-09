"""
CRUD definitions for Team module
"""

from sqlalchemy.orm import Session
from api.teams import models, schemas


def create_team(db: Session, team: schemas.TeamCreate):
    """
    CRUD action to create a new team
    """
    # TODO: Add case where first_player_id == second_player_id
    # TODO: Add case where players do not exist
    db_team = models.Team(
        name=team.name,
        first_player_id=team.first_player_id,
        second_player_id=team.second_player_id if team.second_player_id else None,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def get_teams(db: Session):
    """
    CRUD action to read all teams
    """
    return db.query(models.Team).all()
