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


class TeamDoesNotExistException(Exception):
    """
    Exception thrown when a team does not exist
    """

    pass


class SameTeamsGameException(Exception):
    """
    Exception thrown when a games with the same teams is created
    """

    pass
