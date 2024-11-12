import json
from resources.character_repository import CharacterRepository
from domain.entities.character import Character

class InMemoryCharacterRepository(CharacterRepository):
    def __init__(self):
        self.store = {}  # Diccionario en memoria

    def store_character(self, server_id: str, user_id: str, character) -> None:
        key = f"{server_id}-{user_id}"
        self.store[key] = character.to_json()  # Almacena como JSON

    def retrieve_character(self, server_id: str, user_id: str) -> Character:
        key = f"{server_id}-{user_id}"
        character_json = self.store.get(key)
        if character_json:
            return Character.from_json(character_json)
        return None