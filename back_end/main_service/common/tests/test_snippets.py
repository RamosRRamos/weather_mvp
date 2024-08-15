import unittest
import uuid

from common.snippets import genre_to_playlist, get_weather, get_playlist


class UtilityFunctionsTest(unittest.TestCase):

    def test_genre_to_playlist(self):
        """Testa se a função genre_to_playlist retorna o gênero correto com base na temperatura"""
        self.assertEqual(genre_to_playlist(26), "pop")
        self.assertEqual(genre_to_playlist(25), "rock")
        self.assertEqual(genre_to_playlist(15), "rock")
        self.assertEqual(genre_to_playlist(10), "rock")
        self.assertEqual(genre_to_playlist(9), "classical")

    def test_get_weather(self):
        """Testa se a função get_weather retorna uma resposta válida"""
        city = "São Paulo"
        request_code = uuid.uuid4()

        response = get_weather(city, request_code)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("current", data)
        self.assertIn("temp_c", data["current"])

    def test_get_playlist(self):
        """Testa se a função get_playlist retorna uma resposta válida"""
        temperature = 20  # Temperatura dentro da faixa de rock
        request_code = uuid.uuid4()
        response = get_playlist(temperature, request_code)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("playlist", data)
        self.assertTrue(len(data["playlist"]) > 0)


if __name__ == "__main__":
    unittest.main()
