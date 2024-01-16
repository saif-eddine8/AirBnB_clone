#!/usr/bin/python3
"""class of the Review """             
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class          

    Attributes:
        place_id (str): arg one
        user_id (str): arg two
        name (str): arg three
    """

    place_id = ""
    user_id = ""
    name = ""

