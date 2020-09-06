#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"
    name = Column(String(128),
                  nullable=False)

    place_amenity = relationship(
            "Place",
            secondary="place_amenity",
            viewonly=False,
            back_populates="amenities")
