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
    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    likes = relationship('Like', back_populates='user')

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String(114))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship('User', back_populates='comments')
    post_id = Column(Integer, ForeignKey('post.post_id'))
    post = relationship('Post', back_populates='comments')

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    post_text = Column(String(180))
    post_picture = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')

class Like(Base):
    __tablename__ = 'like'
    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship('User', back_populates='likes')

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

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
