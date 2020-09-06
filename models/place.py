#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
                    "place_amenity",
                    Base.metadata,
                    Column(
                        "place_id",
                        String(60),
                        ForeignKey("places.id"),
                        nullable=False),
                    Column(
                        "amenity_id",
                        String(60),
                        ForeignKey("amenities.id"),
                        nullable=False)
                    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete"
    )
    amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            backref="Place"
            )
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """ reviews getter """
            reviews_list = []
            for value in storage.all("Review").values():
                if value.place_id == self.id:
                    reviews_list.append(value)
            return reviews_list

        @property
        def amenities(self):
            """ amenity getter for FileStorage """
            amenities_list = []
            for value in storage.all("Amenity").values():
                if place_amenity.amenity_id == self.amenity_ids:
                    amenities_list.append(value)
            return amenities_list
        
        @amenities.setter
        def amenities(self, object):
            """
            Setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids
            """
            from models.amenity import Amenity
            
            if isinstance(object, Amenity) and object not in self.amenity_ids:
                self.amenity_ids.append(object.id)

