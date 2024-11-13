import unittest
import json
from domain.entities.character import Character, Attributes, Defenses, Resources, Derived, Skills, Skill

class TestCharacterSerialization(unittest.TestCase):

    def setUp(self):
        # Crear una instancia de Character para los tests
        self.character = Character(
            character_id="001",
            name="Test Character",
            attributes=Attributes(
                strength=10,
                speed=12,
                intellect=14,
                willpower=8,
                awareness=9,
                presence=11
            ),
            defenses=Defenses(
                physical=15,
                cognitive=13,
                spiritual=10,
                deflect=8
            ),
            resources=Resources(
                health=20,
                health_max=20,
                focus=5,
                focus_max=5,
                investiture=0,
                investiture_max=0
            ),
            derived=Derived(
                movement=30,
                recovery_die=8,
                senses_range=15
            ),
            skills=Skills(
                athletics=Skill(proficiency=2, modifier=1),
                agility=Skill(proficiency=1, modifier=2),
                heavy_weapons=Skill(proficiency=3, modifier=0),
                light_weapons=Skill(proficiency=2, modifier=1),
                stealth=Skill(proficiency=1, modifier=2),
                thievery=Skill(proficiency=2, modifier=2),
                crafting=Skill(proficiency=3, modifier=3),
                deduction=Skill(proficiency=2, modifier=1),
                discipline=Skill(proficiency=1, modifier=0),
                intimidation=Skill(proficiency=3, modifier=2),
                lore=Skill(proficiency=2, modifier=1),
                medicine=Skill(proficiency=1, modifier=1),
                deception=Skill(proficiency=2, modifier=2),
                insight=Skill(proficiency=2, modifier=1),
                leadership=Skill(proficiency=1, modifier=2),
                perception=Skill(proficiency=2, modifier=1),
                persuasion=Skill(proficiency=1, modifier=2),
                survival=Skill(proficiency=2, modifier=1)
            ),
            expertises=["heavy_weapons", "intimidation"]
        )

    def test_character_to_json(self):
        # Convertir la instancia de Character a JSON
        character_dict = json.loads(json.dumps(self.character, default=lambda o: o.__dict__))
        
        # Verificar que la estructura de datos exportada es un diccionario
        self.assertIsInstance(character_dict, dict)
        self.assertIn("character_id", character_dict)
        self.assertIn("attributes", character_dict)
        
    def test_character_from_json(self):
        # Serializar la instancia a JSON
        character_json = json.dumps(self.character, default=lambda o: o.__dict__)
        
        # Cargar de nuevo desde JSON
        character_data = json.loads(character_json)
        
        # Crear una nueva instancia de Character desde el JSON cargado
        loaded_character = Character(
            character_id=character_data["character_id"],
            name=character_data["name"],
            attributes=Attributes(**character_data["attributes"]),
            defenses=Defenses(**character_data["defenses"]),
            resources=Resources(**character_data["resources"]),
            derived=Derived(**character_data["derived"]),
            skills=Skills(**{k: Skill(**v) for k, v in character_data["skills"].items()}),
            expertises=character_data["expertises"]
        )

        # Verificar que los datos coinciden
        self.assertEqual(self.character.character_id, loaded_character.character_id)
        self.assertEqual(self.character.name, loaded_character.name)
        self.assertEqual(self.character.attributes.strength, loaded_character.attributes.strength)
        self.assertEqual(self.character.defenses.physical, loaded_character.defenses.physical)
        self.assertEqual(self.character.skills.athletics.proficiency, loaded_character.skills.athletics.proficiency)
        self.assertEqual(self.character.expertises, loaded_character.expertises)

if __name__ == '__main__':
    unittest.main()
