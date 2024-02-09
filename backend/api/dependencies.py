"""
FastAPI endpoint dependency declaration
"""

from api.database import SessionLocal


def get_db():
    """
    Initializes and returns database
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
