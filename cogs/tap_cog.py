# commands/tap.py
import d20
import discord
from discord import app_commands
from domain.entities.character import Character
from interactors import roll_interactor
from presenters.roll_presenter import RollPresenter


class TapCommand(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="tap", description="Realiza una tirada de dados.")
    @app_commands.describe(dice="El formato de dados, como 1d20 o 2d6", advantage="Ventaja o desventaja", plot="Activar tirada de trama")
    async def tap(self, interaction: discord.Interaction, dice: str, advantage: str = None, plot: bool = False):
        await RollPresenter(interaction).roll(roll_interactor.roll(dice))

    # @app_commands.command(name="str", description="Realiza una tirada de dados.")
    # @app_commands.describe(advantage="Ventaja o desventaja", plot="Activar tirada de trama")
    # async def str(self, interaction: discord.Interaction, advantage: str = None, plot: bool = False):
    #     server_id = str(interaction.guild_id)
    #     user_id = str(interaction.user.id)
    #     character : Character = self.character_repo.retrieve_character(server_id, user_id)
    #     dice = f"1d20+{character.attributes['strength']}"
    #     try:
    #         if advantage == "adv":
    #             roll1 = d20.roll(dice)
    #             roll2 = d20.roll(dice)
    #             final_roll = max(roll1.total, roll2.total)
    #             rolls_text = f"{roll1} con ventaja comparado con {roll2}"
    #         elif advantage == "dis":
    #             roll1 = d20.roll(dice)
    #             roll2 = d20.roll(dice)
    #             final_roll = min(roll1.total, roll2.total)
    #             rolls_text = f"{roll1} con desventaja comparado con {roll2}"
    #         else:
    #             roll = d20.roll(dice)
    #             final_roll = roll.total
    #             rolls_text = str(roll)

    #         # Crear el embed
    #         embed = discord.Embed(
    #             title="🎲 Resultado de la tirada",
    #             description=f"Tirada de {dice}",
    #             color=discord.Color.blue()
    #         )
    #         embed.add_field(name="Resultado Total", value=str(final_roll), inline=False)
    #         embed.add_field(name="Detalles de tirada", value=rolls_text, inline=False)

    #         # Añadir un campo adicional si plot está activado
    #         if plot:
    #             plot_roll = d20.roll("1d6")
    #             embed.add_field(name="Plot Roll", value=f"{plot_roll.total} (d6)", inline=False)

    #         await interaction.response.send_message(embed=embed)
    #     except d20.RollSyntaxError:
    #         await interaction.response.send_message("Formato de dados inválido. Usa {d20 dice format}, por ejemplo, 1d20 o 2d6.")

async def setup(bot):
    await bot.add_cog(TapCommand(bot))
