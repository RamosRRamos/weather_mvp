from django.urls import reverse
from unittest.mock import patch
from rest_framework.test import APITestCase
import uuid


class WeatherAPIVIEWTest(APITestCase):
    """
    Tests for the WeatherAPIVIEW to ensure the weather API endpoint is working correctly.
    """

    @patch("api.views.get_weather")
    @patch("api.views.save_weather_data.delay")
    def test_get_weather_valid_city(self, mock_save_weather_data, mock_get_weather):
        """
        Ensure we can retrieve weather data for a valid city.
        """
        # Simula a resposta da função get_weather
        mock_get_weather.return_value.json.return_value = {
            "current": {"temp_c": 30},
            "location": {"name": "London"}
        }

        # Gera um UUID para o request_code
        request_code = str(uuid.uuid4())

        # Faz a requisição GET para a API
        response = self.client.get(
            reverse("weather-api"),
            {"city": "London", "request_code": request_code}
        )

        # Verifica se a resposta está correta
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["location"]["name"], "London")
        self.assertEqual(response.data["current"]["temp_c"], 30)

        # Verifica se a tarefa Celery foi chamada corretamente
        mock_save_weather_data.assert_called_once_with(
            "London", 30, mock_get_weather.return_value.json(), uuid.UUID(request_code)
        )

    @patch("api.views.get_weather")
    @patch("api.views.save_weather_data.delay")
    def test_get_weather_city_not_found(self, mock_save_weather_data, mock_get_weather):
        """
        Ensure the API handles a non-existent city correctly.
        """
        # Simula uma resposta de erro da função get_weather
        mock_get_weather.return_value.json.return_value = {
            "error": {"message": "No matching location found."}
        }

        # Gera um UUID para o request_code
        request_code = str(uuid.uuid4())

        # Faz a requisição GET para a API
        response = self.client.get(
            reverse("weather-api"),
            {"city": "UnknownCity", "request_code": request_code}
        )

        # Verifica se a resposta está correta
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"]["message"], "No matching location found.")

        # Verifica se a tarefa Celery não foi chamada
        mock_save_weather_data.assert_not_called()
