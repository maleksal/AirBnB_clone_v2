#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False
        )

    cities = relationship(
        'City',
        backref='state',
        cascade="all, delete"
    )
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage
            from models.city import City

            hold_objects = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    hold_objects.append(city)
            return hold_objects
