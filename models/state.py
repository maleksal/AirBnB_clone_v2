#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, DateTime, String, ForeignKey
from sys import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False
        )

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def city_getter(self):
            from models import storage
            from models.city import City

            hold_objects = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    hold_objects.append(value)
            return hold_objects
