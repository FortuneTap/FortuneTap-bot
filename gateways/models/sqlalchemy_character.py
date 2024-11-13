from sqlalchemy import Column, String, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SQLAlchemyCharacter(Base):
    __tablename__ = 'characters'

    user_id = Column(String, primary_key=True)
    guild_id = Column(String, primary_key=True)
    character_data = Column(JSON)

    def __init__(self, user_id, guild_id, character_data):
        self.user_id = user_id
        self.guild_id = guild_id
        self.character_data = character_data
