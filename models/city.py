#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import models
from os import getenv


class City(BaseModel, Base):
    """ The city class, inherits from Basemodel and Base"""
    __tablename__ = 'cities'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

    else:
        state_id = ""
        name = ""
