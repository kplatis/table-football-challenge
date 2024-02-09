"""
Router declaration for User module
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from api.dependencies import get_db
from api.users import crud, schemas


router = APIRouter()


@router.post("", tags=["Users"], response_model=schemas.User)
async def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create new user
    """
    return crud.create_user(db=db, user=user)


@router.get("", tags=["Users"], response_model=List[schemas.User])
async def get_all_users(db: Session = Depends(get_db)):
    """
    Endpoint to get users
    """
    return crud.get_users(db)
