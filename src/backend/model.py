import json
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

###Base Models valid globally
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    lists = relationship("List", back_populates="user", cascade="all, delete, delete-orphan")

    def as_json(self, relationships=True):
        #basic attributes
        obj = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        return obj


class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key = True)
    name = Column(String)

    def as_json(self,relationships=True):
        #basic attributes
        obj = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return obj

###Tables in relation to user or language or both
class List(Base):
    __tablename__ = 'list'
    id = Column(Integer, primary_key = True)
    name = Column(String)

    #Referenze to user
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="lists")

    #first language
    first_language_id = Column(Integer, ForeignKey('language.id'))
    first_language = relationship("Language", foreign_keys=[first_language_id])

    #second language
    second_language_id = Column(Integer, ForeignKey('language.id'))
    second_language = relationship("Language", foreign_keys=[second_language_id])

    #
    wordpairs = relationship("WordPair", back_populates="llist", cascade="all, delete, delete-orphan")

    def as_json(self, relationships=True):
        #basic attributes
        obj = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        return obj

class WordPair(Base):
    __tablename__ = 'wordpair'
    id = Column(Integer, primary_key = True)
    llist_id = Column(Integer, ForeignKey('list.id'))
    llist = relationship("List", back_populates="wordpairs")
    first = Column(String)
    second = Column(String)

    def as_json(self, relationships=True):
        #basic attributes
        obj = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        if relationship:
            #Add relationships
            obj.list = {l.as_json(relationships=False) for l in self.llist}

        return obj
