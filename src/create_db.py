#!/usr/bin/python3
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.db import get_db_string

Base = declarative_base()

class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    overall = Column(Integer, nullable=False)
    potential = Column(Integer, nullable=False)
    name = Column(String(250), nullable=False)
    position = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    team = Column(String(250), nullable=False)
    nation = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'overall': self.overall,
            'potential': self.potential,
            'name': self.name,
            'position': self.position,
            'age': self.age,
            'team': self.team,
            'nation': self.nation,
        }

if __name__ == '__main__':
    engine = create_engine(get_db_string())
Base.metadata.create_all(engine)

