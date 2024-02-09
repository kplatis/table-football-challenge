"""
Router declaration for User module
"""

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from api.dependencies import get_db
from api.users.crud import create_user
from api.users.schemas import User, UserCreate


router = APIRouter()


@router.post("", tags=["Categories"], response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create new user
    """
    return create_user(db=db, user=user)
