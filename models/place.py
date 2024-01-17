#!/usr/bin/python3
""" class of t Place"""             
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class               
    Attributes:
        city_id (str): one
        user_id (str): two
        name (str): three
        description (str): four
        number_rooms (int): five
        number_bathrooms (int): six
        max_guest (int): sept
        price_by_night (int): eight
        latitude (float): nine
        longitude (float): ten
        amenity_ids (list): eleven
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

