# redis_repository.py

from typing import List, Optional
import redis
from domain.entities.character import Character
from gateways.character_repository import CharacterRepository

class RedisCharacterRepository(CharacterRepository):
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    def save(self, user_id: str, guild_id: str, character: Character):
        character_key = f"{user_id}:{guild_id}"
        character_data = character.to_json()  # Serialización automática a JSON
        self.redis.set(character_key, character_data)

    def get(self, user_id: str, guild_id: str) -> Optional[Character]:
        character_key = f"{user_id}:{guild_id}"
        character_data = self.redis.get(character_key)
        if character_data:
            return Character.from_json(character_data)  # Deserialización automática
        return None

    def get_all_by_user(self, user_id: str) -> List[Character]:
        keys = self.redis.keys(f"{user_id}:*")
        characters = []
        for key in keys:
            character_data = self.redis.get(key)
            if character_data:
                characters.append(Character.from_json(character_data))  # Deserialización
        return characters
