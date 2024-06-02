#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"

        state_id = Column(
            String(length=60),
            ForeignKey("states.id"),
            nullable=False
        )

        name = Column(
            String(length=128),
            nullable=False
        )

        places = relationship(
            'Place',
            backref=backref('cities'),
            cascade='all, delete'
        )

    else:
        state_id = ""
        name = ""
