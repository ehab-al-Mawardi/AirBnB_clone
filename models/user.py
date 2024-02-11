#!/usr/bin/python3
"""
This file inherits from BaseModel
and defines  UserModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
