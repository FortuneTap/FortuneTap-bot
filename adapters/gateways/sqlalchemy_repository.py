# sqlalchemy_repository.py

from typing import List, Optional
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from gateways.models.sqlalchemy_character import SQLAlchemyCharacter, Base
from domain.entities.character import Character
from gateways.character_repository import CharacterRepository

class SQLAlchemyCharacterRepository(CharacterRepository):
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, user_id: str, guild_id: str, character: Character):
        session = self.Session()
        character_data = character.to_json()  # Serialización a JSON

        # Verificar si ya existe otro personaje con el mismo user_id pero diferente guild_id
        existing_character = session.query(SQLAlchemyCharacter).filter_by(
            user_id=user_id, guild_id=guild_id
        ).first()

        if existing_character:
            existing_character.character_data = character_data
        else:
            new_character = SQLAlchemyCharacter(
                user_id=user_id, guild_id=guild_id, character_data=character_data
            )
            session.add(new_character)

        session.commit()
        session.close()

    def get(self, user_id: str, guild_id: str) -> Optional[Character]:
        session = self.Session()
        result = session.query(SQLAlchemyCharacter).filter_by(
            user_id=user_id, guild_id=guild_id
        ).first()
        session.close()

        if result:
            return Character.from_json(result.character_data)  # Deserialización
        return None

    def get_all_by_user(self, user_id: str) -> List[Character]:
        session = self.Session()
        results = session.query(SQLAlchemyCharacter).filter_by(user_id=user_id).all()
        session.close()

        return [Character.from_json(result.character_data) for result in results if result.guild_id is not None]
