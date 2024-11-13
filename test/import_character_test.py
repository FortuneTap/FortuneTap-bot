import unittest
from unittest.mock import patch, AsyncMock
from lxml import etree
from interactors.import_character import import_character_data

class TestImportCharacterData(unittest.IsolatedAsyncioTestCase):

    @patch("interactors.import_character.get_rendered_html")
    @patch("config.REPOSITORY.save")
    async def test_import_character_data(self, mock_save, mock_get_rendered_html):
        # Simula el HTML de prueba
        with open('test/character_test_data.html', 'r') as file:
            mock_html = file.read()
        
        # Mock del HTML renderizado
        mock_get_rendered_html.return_value = mock_html
        
        # Ejecuta la función con URL y IDs de prueba
        url = "https://example.com/character/1234"
        user_id = "test_user"
        guild_id = "test_guild"
        
        character = await import_character_data(url, user_id, guild_id)

        # Verifica algunos datos del personaje
        self.assertEqual(character.name, "Yazbk")  # Ajusta según el nombre en el HTML de prueba
        self.assertEqual(character.character_id, "1234")
        self.assertIsInstance(character.avatar, str)  # Verifica que el avatar sea un enlace o cadena
        self.assertIsInstance(character.attributes.strength, int)  # Verifica los atributos

        # Verifica que la función de guardado fue llamada
        mock_save.assert_called_once_with(user_id, guild_id, character)

        print(character)

if __name__ == "__main__":
    unittest.main()