"""
CRUD definitions for Users module
"""

from sqlalchemy.orm import Session
from api.users.models import User
from api.users.schemas import UserCreate


def create_user(db: Session, user: UserCreate):
    """
    CRUD action to create a new user
    """
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
