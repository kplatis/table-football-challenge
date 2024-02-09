"""
Main application that initializes the table football challenge API
"""

from fastapi import FastAPI

app = FastAPI()


def read_root():
    """
    Handle GET requests to the root endpoint ("/").

    Returns:
        dict: A dictionary containing a simple greeting message.
    """
    return {"Hello": "World"}
