import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


## Draw from SQLAlchemy base
# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250))
#     last_name = Column(String(250))
#     email=Column(String(50), nullable=False)
#     password=Column(String(25), nullable=False)

# class Characters(Base):
#     __tablename__ = 'character'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     eye_color=Column(String(20))
#     gender=Column(String(20))
#     description= Column(String(20))

# class Planets(Base):
#     __tablename__ = 'planets'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     eye_color=Column(String(20))
#     gender=Column(String(20))
#     description= Column(String(20))

# class Favorite_Character(Base):
#     __tablename__ = 'favorite_character'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user= relationship(User)
#     character_id = Column(Integer, ForeignKey('character.id'))
#     character = relationship(Characters)

# class Favorite_Planet(Base):
#     __tablename__ = 'favorite_planet'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user= relationship(User)
#     planet_id = Column(Integer, ForeignKey('planets.id'))
#     planet = relationship(Planets)

class User(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable =False)
    Followers = Column(Integer)
    Following = Column(Integer)
    Description = Column(String(250))
    
class Post(Base):
    __tablename__ = 'Posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('Users.id'))
    person = relationship(User)
    Description = Column(String(250))
    Comments = Column(String(250))
    
class User_Liked_Posts(Base):
    __tablename__ = 'liked_posts_byuser'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user= relationship(User)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    post = relationship(Post)


# class Followers(Base):
#     __tablename__ = 'User_Followers'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     post_id = Column(Integer, ForeignKey('Posts.id'))
#     post = relationship(Post) 
    


def to_dict(self):
        return {}


render_er(Base, 'diagram.png')
