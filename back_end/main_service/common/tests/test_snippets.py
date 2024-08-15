import unittest
import uuid

from common.snippets import genre_to_playlist, get_weather, get_playlist


class UtilityFunctionsTest(unittest.TestCase):
    """
    Test suite for utility functions: genre_to_playlist, get_weather, and get_playlist.
    """

    def test_genre_to_playlist(self):
        """
        Tests if the genre_to_playlist function returns the correct genre based on the temperature.

        Asserts:
            - The function returns "pop" for temperatures above 25°C.
            - The function returns "rock" for temperatures between 10°C and 25°C inclusive.
            - The function returns "classical" for temperatures below 10°C.
        """
        self.assertEqual(genre_to_playlist(26), "pop")
        self.assertEqual(genre_to_playlist(25), "rock")
        self.assertEqual(genre_to_playlist(15), "rock")
        self.assertEqual(genre_to_playlist(10), "rock")
        self.assertEqual(genre_to_playlist(9), "classical")

    def test_get_weather(self):
        """
        Tests if the get_weather function returns a valid response.

        Steps:
            - Passes the city name and a generated request code to the get_weather function.
            - Checks if the response status code is 200 (OK).
            - Verifies that the response contains the "current" weather data with the key "temp_c" for temperature.

        Asserts:
            - The response status code is 200.
            - The "current" key exists in the response JSON.
            - The "current" key contains the "temp_c" key for temperature.
        """
        city = "São Paulo"
        request_code = uuid.uuid4()

        response = get_weather(city, request_code)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("current", data)
        self.assertIn("temp_c", data["current"])

    def test_get_playlist(self):
        """
        Tests if the get_playlist function returns a valid response.

        Steps:
            - Passes the temperature and a generated request code to the get_playlist function.
            - Checks if the response status code is 200 (OK).
            - Verifies that the response contains the "playlist" key with a non-empty list of songs.

        Asserts:
            - The response status code is 200.
            - The "playlist" key exists in the response JSON.
            - The playlist contains at least one song.
        """
        temperature = 20  # Temperature within the rock genre range
        request_code = uuid.uuid4()
        response = get_playlist(temperature, request_code)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("playlist", data)
        self.assertTrue(len(data["playlist"]) > 0)


if __name__ == "__main__":
    unittest.main()
