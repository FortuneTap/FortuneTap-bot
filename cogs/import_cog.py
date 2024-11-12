import discord
from discord.ext import commands
from discord import app_commands
from presenters.character_presenter import CharacterPresenter
from interactors import import_character

class ImportCharacter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="import", description="Importa un personaje desde Demiplane con la URL de su hoja.")
    async def import_character(self, interaction: discord.Interaction, url: str):
        """Comando de Discord para importar un personaje desde Demiplane."""
        await interaction.response.defer()

        # await CharacterPresenter(interaction).show()

        try:
            character = await import_character.import_character_data(url)
        except Exception as e:
            print(e)

        print(character)

        embed = discord.Embed(
            title=f"Datos del Personaje: {character.name}",
            color=discord.Color.gold(),
        )
        embed.set_thumbnail(url = character.avatar)
        embed.add_field(name="Strength", value=character.attributes.strength, inline=False)

        await interaction.followup.send(embed=embed)

# Configuración para añadir el cog al bot
async def setup(bot):
    await bot.add_cog(ImportCharacter(bot))
