"""
CRUD definitions for Users module
"""

from sqlalchemy.orm import Session
from api.users import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    """
    CRUD action to create a new user
    """
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    """
    CRUD action get users
    """
    return db.query(models.User).all()
