#!/usr/bin/python3
"""Definition of the State class and Base instance using SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class
Base = declarative_base()

class State(Base):
    """Class that represents a state in the states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
