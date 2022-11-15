import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()




class User(Base):
                    __tablename__ = 'user'
                    id = Column(Integer, primary_key=True)
                    username = Column(String(250), nullable=False)
                    name = Column(String(250), nullable=False)
                    lastname = Column(String(250), nullable=False)
                    email = Column(String(250), nullable=False)
                    password = Column(String(250), nullable=False)
                    friends = relationship("User", secondary="friendship")
                    favourites_characters = relationship("Favourites_characters", back_populates="user")
                    favourites_planets = relationship("Favourites_planets", back_populates="user")
                    favourites_starships = relationship("Favourites_starships", back_populates="user")
                    favourites_vehicles = relationship("Favourites_vehicles", back_populates="user")
                    favourites_species = relationship("Favourites_species", back_populates="user")
                    favourites_films = relationship("Favourites_films", back_populates="user")
                    created = Column(Date(), nullable=False)
                    last_login_date = Column(Date(), nullable=False)

                    
class Friendship(Base):
                    __tablename__ = 'friendship'
                    id = Column(Integer, primary_key=True)
                    user_id = Column(Integer, ForeignKey('user.id'))
                    friend_id = Column(Integer, ForeignKey('user.id'))




class Thread(Base):
                    __tablename__ = 'thread'
                    id = Column(Integer, primary_key=True)
                    user_id = Column(Integer, ForeignKey('user.id'))
                    message = Column(String(250), nullable=False)
                    user = relationship(User)

class Forum (Base):
                    __tablename__ = 'forum'
                    id = Column(Integer, primary_key=True)
                    user_id = Column(Integer, ForeignKey('user.id'))
                    thread_id = Column(Integer, ForeignKey('thread.id'))
                    user = relationship(User)
                    thread = relationship(Thread)

class Private_message(Base):
                    __tablename__ = 'private_message'
                    id = Column(Integer, primary_key=True)
                    user_id = Column(Integer, ForeignKey('user.id'))
                    message = Column(String(250), nullable=False)
                    user = relationship(User)          

class User_session(Base):
                    __tablename__ = 'user_session'
                    id = Column(Integer, primary_key=True)
                    user_id = Column(Integer, ForeignKey('user.id'))
                    token = Column(String(250), nullable=False)
                    user = relationship(User)                       




class Planet(Base):
                    __tablename__ = 'planet'
                    id = Column(Integer, primary_key=True)
                    name = Column(String(250), nullable=False)
                    rotation_period = Column(Integer, nullable=False)
                    orbital_period = Column(Integer, nullable=False)
                    diameter = Column(Integer, nullable=False)
                    climate = Column(String(250), nullable=False)
                    gravity = Column(String(250), nullable=False)
                    terrain = Column(String(250), nullable=False)
                    surface_water = Column(Integer, nullable=False)
                    population = Column(Integer, nullable=False)
                    residents = Column(String(250), nullable=False)
                    films = Column(String(250), nullable=False)
                    created = Column(String(250), nullable=False)
                    edited = Column(String(250), nullable=False)
                    url = Column(String(250), nullable=False)

class Starship(Base):
                    __tablename__ = 'starship'
                    id = Column(Integer, primary_key=True)
                    name = Column(String(250), nullable=False)
                    model = Column(String(250), nullable=False)
                    starship_class = Column(String(250), nullable=False)
                    manufacturer = Column(String(250), nullable=False)
                    cost_in_credits = Column(Integer, nullable=False)
                    length = Column(Integer, nullable=False)
                    crew = Column(Integer, nullable=False)
                    passengers = Column(Integer, nullable=False)
                    max_atmosphering_speed = Column(Integer, nullable=False)
                    hyperdrive_rating = Column(Integer, nullable=False)
                    mglt = Column(Integer, nullable=False)
                    cargo_capacity = Column(Integer, nullable=False)
                    consumables = Column(String(250), nullable=False)
                    films = Column(String(250), nullable=False)
                    pilots = Column(String(250), nullable=False)
                    created = Column(String(250), nullable=False)
                    edited = Column(String(250), nullable=False)
                    url = Column(String(250), nullable=False)

class Vehicle(Base):
                    __tablename__ = 'vehicle'
                    id = Column(Integer, primary_key=True)
                    name = Column(String(250), nullable=False)
                    model = Column(String(250), nullable=False)
                    vehicle_class = Column(String(250), nullable=False)
                    manufacturer = Column(String(250), nullable=False)
                    cost_in_credits = Column(Integer, nullable=False)
                    length = Column(Integer, nullable=False)
                    crew = Column(Integer, nullable=False)
                    passengers = Column(Integer, nullable=False)
                    max_atmosphering_speed = Column(Integer, nullable=False)
                    cargo_capacity = Column(Integer, nullable=False)
                    consumables = Column(String(250), nullable=False)
                    films = Column(String(250), nullable=False)
                    pilots = Column(String(250), nullable=False)
                    created = Column(String(250), nullable=False)
                    edited = Column(String(250), nullable=False)
                    url = Column(String(250), nullable=False)

class Species(Base):
                    __tablename__ = 'species'
                    id = Column(Integer, primary_key=True)
                    name = Column(String(250), nullable=False)
                    classification = Column(String(250), nullable=False)
                    designation = Column(String(250), nullable=False)
                    average_height = Column(Integer, nullable=False)
                    skin_colors = Column(String(250), nullable=False)
                    hair_colors = Column(String(250), nullable=False)
                    eye_colors = Column(String(250), nullable=False)
                    average_lifespan = Column(Integer, nullable=False)
                    homeworld = Column(String(250), nullable=False)
                    language = Column(String(250), nullable=False)
                    people = Column(String(250), nullable=False)
                    films = Column(String(250), nullable=False)
                    created = Column(String(250), nullable=False)
                    edited = Column(String(250), nullable=False)
                    url = Column(String(250), nullable=False)

class Films(Base):
                    __tablename__ = 'films'
                    id = Column(Integer, primary_key=True)
                    title = Column(String(250), nullable=False)
                    episode_id = Column(Integer, nullable=False)
                    opening_crawl = Column(String(250), nullable=False)
                    director = Column(String(250), nullable=False)
                    producer = Column(String(250), nullable=False)
                    release_date = Column(String(250), nullable=False)
                    characters = Column(String(250), nullable=False)
                    planets = Column(String(250), nullable=False)
                    starships = Column(String(250), nullable=False)
                    vehicles = Column(String(250), nullable=False)
                    species = Column(String(250), nullable=False)
                    created = Column(String(250), nullable=False)
                    edited = Column(String(250), nullable=False)
                    url = Column(String(250), nullable=False)

class Character(Base):
                    __tablename__ = 'character'
                    id = Column(Integer, primary_key=True)
                    name = Column(String(250), nullable=False)
                    height = Column(Integer, nullable=False)
                    mass = Column(Integer, nullable=False)
                    hair_color = Column(String(250), nullable=False)
                    skin_color = Column(String(250), nullable=False)
                    eye_color = Column(String(250), nullable=False)
                    birth_year = Column(String(250), nullable=False)
                    gender = Column(String(250), nullable=False)
                    homeworld = Column(String(250), ForeignKey('planet.url'), nullable=False)
                    homeworld = relationship(Planet)
                    films = Column(String(250), ForeignKey('films.url'), nullable=False)
                    films = relationship(Films)
                    species = Column(String(250), ForeignKey('species.url'), nullable=False)
                    species = relationship(Species)
                    vehicles = Column(String(250), ForeignKey('vehicle.url'), nullable=False)
                    vehicles = relationship(Vehicle)
                    starships = Column(String(250), ForeignKey('starship.url'), nullable=False)
                    starships = relationship(Starship)
                    created = Column(String(250), nullable=False)
                    edited = Column(String(250), nullable=False)
                    url = Column(String(250), nullable=False)

class Homeworld(Base):
                    __tablename__ = 'homeworld'
                    id = Column(Integer, primary_key=True)
                    planet_id = Column(Integer, ForeignKey('planet.id'))
                    character_id = Column(Integer, ForeignKey('character.id'))
                    planet = relationship(Planet)
                    character = relationship(Character)

class Character_species(Base):
                    __tablename__ = 'character_species'
                    id = Column(Integer, primary_key=True)
                    character_id = Column(Integer, ForeignKey('character.id'))
                    species_id = Column(Integer, ForeignKey('species.id'))
                    character = relationship(Character)
                    species = relationship(Species)

class Character_film(Base):
                    __tablename__ = 'character_film'
                    id = Column(Integer, primary_key=True)
                    character_id = Column(Integer, ForeignKey('character.id'))
                    film_id = Column(Integer, ForeignKey('films.id'))
                    character = relationship(Character)
                    film = relationship(Films)

class Starship_film(Base):
                    __tablename__ = 'starship_film'
                    id = Column(Integer, primary_key=True)
                    starship_id = Column(Integer, ForeignKey('starship.id'))
                    film_id = Column(Integer, ForeignKey('films.id'))
                    starship = relationship(Starship)
                    film = relationship(Films)

class Character_vehicle(Base):
                    __tablename__ = 'character_vehicle'
                    id = Column(Integer, primary_key=True)
                    character_id = Column(Integer, ForeignKey('character.id'))
                    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
                    character = relationship(Character)
                    vehicle = relationship(Vehicle)

class Favourites(Base):
                    __tablename__ = 'favourites'
                    id = Column(Integer, primary_key=True)
                    user_id = Column(Integer, ForeignKey('user.id'))
                    user = relationship(User)
                    character_id = Column(Integer, ForeignKey('character.id'))
                    character = relationship(Character)
                    planet_id = Column(Integer, ForeignKey('planet.id'))
                    planet = relationship(Planet)
                    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
                    vehicle = relationship(Vehicle)
                    species_id = Column(Integer, ForeignKey('species.id'))
                    species = relationship(Species)
                    starship_id = Column(Integer, ForeignKey('starship.id'))
                    starship = relationship(Starship)
                    films_id = Column(Integer, ForeignKey('films.id'))
                    films = relationship(Films)


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
