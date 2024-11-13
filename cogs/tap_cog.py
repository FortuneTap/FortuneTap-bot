import discord
from discord import app_commands
from domain.entities.character import Character
from interactors import roll_interactor
from presenters.roll_presenter import RollPresenter
import config
import traceback

class TapCommand(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="roll", description="Realiza una tirada de dados.")
    @app_commands.describe(dice="El formato de dados, como 1d20 o 2d6", advantage="Ventaja o desventaja", plot="Activar tirada de trama")
    async def roll(self, interaction: discord.Interaction, dice: str, advantage: str = None, plot: bool = False):
        await RollPresenter(interaction).roll(roll_interactor.roll(dice))

    @app_commands.command(name="tap", description="Realiza una tirada usando un atributo o habilidad.")
    @app_commands.describe(
        stat="El atributo o habilidad a usar en la tirada",
        dice="El formato de dados, como 1d20 o 2d6"
    )
    @app_commands.choices(
        stat=[
            # Opciones de Atributos
            app_commands.Choice(name="Strength", value="attributes.strength"),
            app_commands.Choice(name="Speed", value="attributes.speed"),
            app_commands.Choice(name="Intellect", value="attributes.intellect"),
            app_commands.Choice(name="Willpower", value="attributes.willpower"),
            app_commands.Choice(name="Awareness", value="attributes.awareness"),
            app_commands.Choice(name="Presence", value="attributes.presence"),
            # Opciones de Habilidades (Skills)
            app_commands.Choice(name="Athletics", value="skills.athletics"),
            app_commands.Choice(name="Agility", value="skills.agility"),
            app_commands.Choice(name="Heavy Weapons", value="skills.heavy_weapons"),
            app_commands.Choice(name="Light Weapons", value="skills.light_weapons"),
            app_commands.Choice(name="Stealth", value="skills.stealth"),
            app_commands.Choice(name="Thievery", value="skills.thievery"),
            app_commands.Choice(name="Crafting", value="skills.crafting"),
            app_commands.Choice(name="Deduction", value="skills.deduction"),
            app_commands.Choice(name="Discipline", value="skills.discipline"),
            app_commands.Choice(name="Intimidation", value="skills.intimidation"),
            app_commands.Choice(name="Lore", value="skills.lore"),
            app_commands.Choice(name="Medicine", value="skills.medicine"),
            app_commands.Choice(name="Deception", value="skills.deception"),
            app_commands.Choice(name="Insight", value="skills.insight"),
            app_commands.Choice(name="Leadership", value="skills.leadership"),
            app_commands.Choice(name="Perception", value="skills.perception"),
            app_commands.Choice(name="Persuasion", value="skills.persuasion"),
            app_commands.Choice(name="Survival", value="skills.survival"),
        ]
    )
    async def tap(self, interaction: discord.Interaction, stat: app_commands.Choice[str], dice: str = "1d20"):
        """Realiza una tirada de dados usando un atributo o habilidad del personaje activo."""

        user_id = str(interaction.user.id)
        guild_id = str(interaction.guild.id)

        try:
            # Obtener el personaje activo del usuario en el servidor actual
            character = config.REPOSITORY.get(user_id, guild_id)

            if character:
                # Determinar si el stat es un atributo o habilidad
                stat_category, stat_name = stat.value.split(".")

                if stat_category == "attributes":
                    # Obtener el valor del atributo
                    modifier = getattr(character.attributes, stat_name, None)
                elif stat_category == "skills":
                    # Obtener el valor de la habilidad (modificador dentro de Skill)
                    skill = getattr(character.skills, stat_name, None)
                    modifier = skill.modifier if skill else None
                else:
                    modifier = None

                if modifier is not None:
                    # Realizar la tirada de dados con el modificador
                    roll_result = roll_interactor.roll(f"{dice}+{modifier}")
                    await RollPresenter(interaction).roll(roll_result, title = f"Tapping {stat_name} 🎲")
                else:
                    await interaction.response.send_message(
                        "El personaje no tiene un valor válido para el atributo o habilidad seleccionado.",
                        ephemeral=True
                    )
            else:
                await interaction.response.send_message(
                    "No tienes un personaje activo en este servidor.",
                    ephemeral=True
                )

        except Exception as e:
            await interaction.response.send_message(
                "Ha ocurrido un error inesperado. Inténtalo de nuevo más tarde.",
                ephemeral=True
            )
            print(f"Error inesperado: {e}")


async def setup(bot):
    await bot.add_cog(TapCommand(bot))
