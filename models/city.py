#!/usr/bin/python3
""" Module for City class """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ City class """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)

    places = relationship("Place", cascade="all, delete", backref="cities")
