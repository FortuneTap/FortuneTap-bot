from gateways.in_memory_character_repository import InMemoryCharacterRepository
from gateways.character_repository import CharacterRepository
from dotenv import load_dotenv
import os

# Cargar el token desde el archivo .env
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Inicializamos el repositorio de memoria
REPOSITORY : CharacterRepository = InMemoryCharacterRepository()
