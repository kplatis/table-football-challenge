"""
Main application that initializes the table football challenge API
"""

from fastapi import FastAPI
from api.database import Base, engine
from api.users import routers as user_routers

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations related to users",
    }
]

app = FastAPI(openapi_tags=tags_metadata)


app.include_router(user_routers.router, prefix="/users")
