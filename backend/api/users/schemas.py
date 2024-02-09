"""
Schema declaration for Users module
"""

from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base schema declaration for User
    """

    name: str


class UserCreate(UserBase):
    """
    Schema declaration for creation of User
    """

    pass


class User(UserBase):
    """
    Schema declaration for User
    """

    id: int
