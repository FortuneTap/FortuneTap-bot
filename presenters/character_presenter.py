import discord
import d20

from domain.entities.character import Character

class CharacterPresenter:
    interaction: discord.Interaction

    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction

    async def show(self, character: Character):
        embed = discord.Embed(
            title=f"Datos del Personaje: {character.name}",
            color=discord.Color.gold()
        )
        embed.add_field(name="Strength", value=character.attributes.strength, inline=False)

        await self.interaction.followup.send(embed=embed)
