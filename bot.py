import discord
from discord.ext import commands
import asyncio
import adapters.config as config

# Configuración de los intents y el cliente del bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# Evento on_ready para sincronizar los comandos de barra
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} está listo y los comandos slash están sincronizados.")

# Cargar los módulos de comandos
async def load_extensions():
    await bot.load_extension("cogs.tap_cog")
    await bot.load_extension("cogs.character_cog")

# Ejecutar el bot
async def main():
    await load_extensions()
    await bot.start(config.DISCORD_TOKEN)


asyncio.run(main())
