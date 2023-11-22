#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class inherits from Basemodel and Base"""
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        name = ""

    @property
    def cities(self):
        """returns the list of City instances with state_id
        equals to the current State.id => It will be the FileStorage
        relationship between State and City
        """

        cities = []
        for city in models.storage.all("City").values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
