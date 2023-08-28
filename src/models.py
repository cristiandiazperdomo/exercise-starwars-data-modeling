import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)

class Starships(Base):
    __tablename__ = 'starship'

    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    people_id = Column(Integer, ForeignKey('people.people_id'))
    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'))
    starships_id = Column(Integer, ForeignKey('starship.starship_id'))

    usuario = relationship(User)
    planets = relationship(Planets)
    people = relationship(People)
    vehicles = relationship(Vehicles)
    starships = relationship(Starships)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
