#!/usr/bin/python3
"""
Defines the Place model,
that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """place model"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = []
