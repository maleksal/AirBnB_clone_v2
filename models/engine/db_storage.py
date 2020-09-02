#!/usr/bin/python3
"""This module defines a class to manage storage for hbnb clone"""
import os
from sqlalchemy.engine import create_engine


class DBStorage:
    """This class manages storage of hbnb models."""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage class constructor """
        from models.base_model import Base

        self.__engine = create_engine(
                        'mysql+mysqldb://{}:{}@{}/{}'.
                        format(
                            os.getenv("HBNB_MYSQL_USER"),
                            os.getenv("HBNB_MYSQL_PWD"),
                            os.getenv("HBNB_MYSQL_HOST"),
                            os.getenv("HBNB_MYSQL_DB")
                        ), pool_pre_ping=True)
        # Drop all tables in test env
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all objects
        depending of the class name (argument cls). if cls=None, query all
        types of objects (User, State, City, Amenity, Place and Review).

        Returns:
            this method return a dictionary: (like FileStorage)
                key = <class-name>.<object-id>
                value = object
        """

        def append_object(dic, query):
            """ Appends an object to a dictionary, with specific key format.

                Returns:
                    this function returns a dictionary with:
                    key: <obj.name>.<obj.id>
                    value: obj
            """
            if query:
                for object in query:
                    dic[type(object).__name__ + '.' + object.id] = object

        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User

        queried_data = {}
        models = [State, City, Place, Amenity, Review, User]

        if cls:
            cls = cls.__name__
            append_object(queried_data, self.__session.query(eval(cls)).all())
        else:
            for model in models:
                append_object(queried_data, self.__session.query(eval(model)))
        return queried_data

    def new(self, obj):
        """Adds an object to the current database session """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and create the current
        database session (self.__session) from the engine (self.__engine).
        """
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import Base
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
                                bind=self.__engine,
                                expire_on_commit=False
                                ))
        self.__session = Session()

    def close(self):
        """ call close() on the class Session """
        self.__session.close()
