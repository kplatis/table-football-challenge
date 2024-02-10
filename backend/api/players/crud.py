"""
CRUD definitions for Players module
"""

from sqlalchemy.orm import Session
from api.players import models, schemas


def create_player(db: Session, player: schemas.PlayerCreate):
    """
    CRUD action to create a new player
    """
    db_player = models.Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


def get_players(db: Session):
    """
    CRUD action get players
    """
    return db.query(models.Player).all()
