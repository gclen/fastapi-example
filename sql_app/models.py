from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import RelationshipProperty

from .database import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    team = Column(String(64), index=True, unique=True)
    wins = Column(Integer, index=True)

