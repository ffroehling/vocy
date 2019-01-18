from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

###Base Models valid globally
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String)

class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key = True)
    name = Column(String)

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
    first_language = relationship("Language")

    #second language
    second_language_id = Column(Integer, ForeignKey('language.id'))
    second_language = relationship("Language")

class WordPair(Base):
    __tablename__ = 'wordpair'
    id = Column(Integer, primary_key = True)
    llist_id = Column(Integer, ForeignKey('list.id'))
    llist = relationship("List", back_populates="wordpairs")
     



