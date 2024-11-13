from gateways.in_memory_character_repository import InMemoryCharacterRepository
from gateways.character_repository import CharacterRepository
from dotenv import load_dotenv
import os
from gateways.caching_character_repository import CachingCharacterRepository
import redis


# Cargar el token desde el archivo .env
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
REDIS_URL = os.getenv('REDIS_URL')  # URL de conexión de Redis
POSTGRES_URL = os.getenv('POSTGRES_URL')  # URL de conexión de PostgreSQL

# Configurar cliente Redis
redis_client = redis.Redis.from_url(REDIS_URL)

# Inicializar el repositorio de caching
REPOSITORY: CharacterRepository = CachingCharacterRepository(redis_client, POSTGRES_URL)
