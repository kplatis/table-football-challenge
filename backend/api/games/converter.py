from api.games import schemas as games_schemas, models
from api.teams import schemas as teams_schemas
from api.players import schemas as players_schemas


def convert_game_model_to_schema(game: models.Game):
    """
    Converts an SQLAlchemy model to a pydantic schema
    """
    return games_schemas.Game.model_validate(
        {
            **game.__dict__,
            "first_team": teams_schemas.Team.model_validate(
                {
                    **game.first_team.__dict__,
                    "first_player": players_schemas.Player.model_validate(
                        game.first_team.first_player.__dict__
                    ),
                    "second_player": (
                        players_schemas.Player.model_validate(
                            game.first_team.second_player.__dict__
                        )
                        if game.first_team.second_player
                        else None
                    ),
                }
            ),
            "second_team": teams_schemas.Team.model_validate(
                {
                    **game.second_team.__dict__,
                    "first_player": players_schemas.Player.model_validate(
                        game.second_team.first_player.__dict__
                    ),
                    "second_player": (
                        players_schemas.Player.model_validate(
                            game.second_team.second_player.__dict__
                        )
                        if game.second_team.second_player
                        else None
                    ),
                }
            ),
        }
    )
