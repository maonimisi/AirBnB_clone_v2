#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """
    This is the class for Amenity
        Attributes:
            name - input name
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates='amenities')
