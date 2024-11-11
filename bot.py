import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from resources.in_memory_character_repository import InMemoryCharacterRepository

# Cargar el token desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configuración de los intents y el cliente del bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Evento on_ready para sincronizar los comandos de barra
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} está listo y los comandos slash están sincronizados.")

character_repo = InMemoryCharacterRepository()
# Cargar los módulos de comandos
async def load_extensions():
    await bot.load_extension("cogs.tap_cog")
    await bot.load_extension("cogs.import_cog", character_repo=character_repo)

# Ejecutar el bot
async def main():
    await load_extensions()
    await bot.start(TOKEN)

import asyncio
asyncio.run(main())
