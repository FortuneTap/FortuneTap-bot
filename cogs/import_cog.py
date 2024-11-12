import discord
from discord.ext import commands
from discord import app_commands
from domain.entities.character import Character
from services import import_character

class ImportCharacter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="import", description="Importa un personaje desde Demiplane con la URL de su hoja.")
    async def import_character(self, interaction: discord.Interaction, url: str):
        """Comando de Discord para importar un personaje desde Demiplane."""
        await interaction.response.send_message("Importando personaje...", ephemeral=True)

        try:
            # Llama a la función de extracción de datos
            character : Character = await import_character.import_character_data(url)
        except Exception as e:
            print(e.__traceback__)
            await interaction.followup.send(f"Error al obtener datos del personaje: {e}")
            return
        
        # Almacena el personaje en el repositorio
        server_id = str(interaction.guild_id)
        user_id = str(interaction.user.id)
        #self.character_repo.store_character(server_id, user_id, character)

        # Crear el embed
        embed = discord.Embed(title=f"Datos del Personaje: {character.name}", color=discord.Color.blue())

        # Agregar atributos al embed
        attributes_text = "\n".join([f"**{key.capitalize().replace('_', ' ')}:** {value}" 
                                     for key, value in character.attributes.items()])
        embed.add_field(name="Atributos", value=attributes_text, inline=False)

        # Agregar habilidades al embed
        skills_text = "\n".join([f"**{key}:** {value}" for key, value in character.skills.items()])
        embed.add_field(name="Habilidades", value=skills_text, inline=False)

        # Enviar el embed como respuesta de seguimiento
        await interaction.followup.send(embed=embed)

# Configuración para añadir el cog al bot
async def setup(bot):
    await bot.add_cog(ImportCharacter(bot))
