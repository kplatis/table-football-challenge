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
    db_team = models.Team(
        name=team.name,
        first_player_id=team.first_player_id,
        second_player_id=team.second_player_id,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
