#!/usr/bin/python3
'''
creating city class
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    '''
    class city that inherits from Base
    '''
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=True, primary_key=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=True)
