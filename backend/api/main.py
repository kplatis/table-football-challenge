"""
Main application that initializes the table football challenge API
"""

from fastapi import FastAPI
from api.database import Base, engine
from api.users import routers as user_routers

Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(user_routers.router, prefix="/users")
