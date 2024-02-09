"""
Router declaration for User module
"""

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from api.dependencies import get_db
from api.users import crud, schemas


router = APIRouter()


@router.post("", tags=["Categories"], response_model=schemas.User)
async def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create new user
    """
    return crud.create_user(db=db, user=user)
