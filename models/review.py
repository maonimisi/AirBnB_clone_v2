#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Model
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information 
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('place_id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
