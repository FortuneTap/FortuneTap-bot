from abc import ABC, abstractmethod
from domain.entities.character import Character

class CharacterRepository(ABC):
    @abstractmethod
    def store_character(self, server_id: str, user_id: str, character) -> None:
        """Almacena un personaje para un usuario específico en un servidor."""
        pass

    @abstractmethod
    def retrieve_character(self, server_id: str, user_id: str) -> Character:
        """Recupera un personaje para un usuario específico en un servidor."""
        pass