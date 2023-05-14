#!/usr/bin/python3
"""
Module: city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city's model.

    Attributes:
        name
        state_id
    """
    state_id = ""
    name = ""
