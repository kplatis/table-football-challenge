"""
Main application that initializes the table football challenge API
"""

from fastapi import FastAPI
from api.users import routers as user_routers


app = FastAPI()


app.include_router(user_routers, prefix="/users")
