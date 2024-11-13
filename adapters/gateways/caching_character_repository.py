from typing import List, Optional
from domain.entities.character import Character
from gateways.character_repository import CharacterRepository
from gateways.redis_character_repository import RedisCharacterRepository
from gateways.sqlalchemy_repository import SQLAlchemyCharacterRepository

class CachingCharacterRepository(CharacterRepository):
    def __init__(self, redis_client, db_url: str):
        self.redis_repo = RedisCharacterRepository(redis_client)
        self.sqlalchemy_repo = SQLAlchemyCharacterRepository(db_url)

    def save(self, user_id: str, guild_id: str, character: Character):
        # Guardar en Redis y PostgreSQL
        self.redis_repo.save(user_id, guild_id, character)
        self.sqlalchemy_repo.save(user_id, guild_id, character)

    def get(self, user_id: str, guild_id: str) -> Optional[Character]:
        # Intentar recuperar desde Redis primero
        character = self.redis_repo.get(user_id, guild_id)
        
        # Si no está en Redis, intentar en PostgreSQL y guardar en Redis si se encuentra
        if not character:
            character = self.sqlalchemy_repo.get(user_id, guild_id)
            if character:
                self.redis_repo.save(user_id, guild_id, character)  # Cachearlo en Redis

        return character

    def get_all_by_user(self, user_id: str) -> List[Character]:
        # Recuperar todos los personajes del usuario desde PostgreSQL
        characters = self.sqlalchemy_repo.get_all_by_user(user_id)
        
        # Guardar cada personaje en Redis para futuras consultas
        for character in characters:
            self.redis_repo.save(user_id, character.guild_id, character)

        return characters
