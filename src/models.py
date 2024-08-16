import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(25), nullable=False)
    email = Column(String(255), nullable=False)
    pass_user = Column(String(40), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    post_text = Column(String(180))
    post_picture = Column(String(255))
    user_post = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)
                       
class Likes(Base):
    __tablename__ ='likes'
    like_id = Column(Integer, primary_key=True)
    like_user = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)

class Coment(Base):
    __tablename__ ='coment'
    coment_id = Column(Integer, primary_key=True)
    coment_text = Column(String(114))
    user_coment = Column(String(114), ForeignKey('user.user_id'))
    user = relationship(User)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
