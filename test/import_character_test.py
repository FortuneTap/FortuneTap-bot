import unittest
import requests_mock
from services import import_character
import os

class TestImportCharacterData(unittest.TestCase):
    maxDiff = None  # Esto permite ver el diff completo

    @requests_mock.Mocker()
    def test_import_character_data(self, mock_request):
        # Ruta al archivo HTML de prueba
        file_path = os.path.join(os.path.dirname(__file__), 'character_test_data.html')
        
        # Lee el contenido del archivo HTML de prueba
        with open(file_path, 'r', encoding='utf-8') as file:
            mock_html = file.read()

        # URL simulada y configuración del mock para que devuelva el HTML del archivo
        url = "https://app.demiplane.com/nexus/cosmererpg/character-sheet/7a022a6b-b70a-4adf-9fa4-f830ca02afa7"
        mock_request.get(url, text=mock_html)

        # Ejecuta la función
        character_data = import_character.import_character_data(url)

        # Verifica los valores de atributos esperados
        expected_attributes = {
            "strength": "1",
            "speed": "2",
            "defense_physical": "13",
            "defense_cognitive": "16",
            "defense_spiritual": "13",
            "movement": "25 ft.",
            "recovery_die": "d8",
            "senses_range": "10 ft.",
            "health": "/11",
            "focus": "/5",
            "investiture": "/0"
        }
        self.assertEqual(character_data["attributes"], expected_attributes)

        # Verifica los valores de habilidades esperados
        expected_skills = {
            "Athletics": "+2",
            "Agility": "+3"
        }
        self.assertEqual(character_data["skills"], expected_skills)

if __name__ == "__main__":
    unittest.main()
