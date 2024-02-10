"""
Module defining the custom exceptions
"""


class PlayerDoesNotExistException(Exception):
    """
    Exception thrown when a player does not exist
    """

    pass


class SamePlayersTeamException(Exception):
    """
    Exception thrown when a team with the same player is created
    """

    pass
