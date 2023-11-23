#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage_type


class State(BaseModel, Base):
    """ State class inherits from Basemodel and Base"""
    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """returns the list of City instances with state_id
        equals to the current State.id => It will be the FileStorage
        relationship between State and City
        """

        citiesList = []
        citiesAll = storage.all(City)
        for city in citiesAll.values():
            if city.state_id == self.id:
                citiesList.append(city)
        return citiesList
