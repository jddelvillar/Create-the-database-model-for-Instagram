import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class comments(Base):
    __tablename__='comments'
    idComm = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer)
    post_id = Column(Integer)
   

class Media(Base):
    __tablename__='media'
    idMed = Column(Integer, primary_key=True)
    Type = Column(String(250))
    Url = Column(String(250))
    post_id = Column(Integer)
    
class Users(Base):
    __tablename__='users'
    userId = Column(Integer, primary_key=True)
    idComm = Column(Integer, ForeignKey('comments.idComm'))
    idMed = Column(Integer, ForeignKey('media.idMed'))
    Username = Column(String(250))
    Firstsname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(150))
    comments = relationship(comments)
    Media = relationship(Media)
    

class Favorites(Base):
    __tablename__='favorites'
    favId = Column(Integer, primary_key=True)
    idComm = Column(Integer, ForeignKey('comments.idComm'))
    idMed = Column(Integer, ForeignKey('media.idMed'))
    userId = Column(Integer, ForeignKey('users.userId'))
    comments = relationship(comments)
    Media = relationship(Media)
    users = relationship(Users)
   
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e