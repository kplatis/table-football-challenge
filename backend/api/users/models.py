"""
Model declaration for users module
"""

from sqlalchemy import Column, Integer, String
from api.database import Base


class User(Base):
    """
    SQLAlchemy model defining the user model
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
