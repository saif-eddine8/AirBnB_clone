#!/usr/bin/python3
"""class of the User """                   
from models.base_model import BaseModel


class User(BaseModel):
    """User class                         
    Attributes:
        email (str): one
        password (str): two
        first_name (str): three
        last_name (str): four
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

