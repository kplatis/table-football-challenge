"""
Main application that initializes the table football challenge API
"""

from fastapi import FastAPI
from api.database import Base, engine
from api.teams import routers as team_routers
from api.players import routers as players_routers


Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "Players",
        "description": "Operations related to players",
    },
    {
        "name": "Teams",
        "description": "Operations related to teams",
    },
]

app = FastAPI(openapi_tags=tags_metadata)


app.include_router(players_routers.router, prefix="/players")
app.include_router(team_routers.router, prefix="/teams")
