import uuid
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.snippets import get_weather, float_temperature, get_playlist

class PlaylistView(APIView):
    """
    API view to retrieve a music playlist based on the current weather of a specified city.

    This view handles GET requests and requires a city name to fetch the weather information.
    Based on the temperature obtained from the weather data, it requests a corresponding music playlist.

    Permission:
        - AllowAny: This view is accessible without authentication.

    Methods:
        - get: Handles GET requests to retrieve the playlist based on the city's weather.
    """

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to return a music playlist based on the weather of a specified city.

        Query Parameters:
            - city (str): The name of the city for which the weather and playlist are requested.

        Generates a unique request code for tracking purposes.

        Workflow:
            1. Fetches the current weather data for the specified city.
            2. Extracts the temperature from the weather data.
            3. Requests a music playlist based on the extracted temperature.

        Returns:
            - HTTP 200 OK: If the playlist is successfully retrieved.
            - HTTP 400 Bad Request: If the city parameter is missing.
            - HTTP 500 Internal Server Error: If there's an issue fetching the weather or playlist data.
        """
        city = request.query_params.get("city")
        request_code = uuid.uuid4()

        if not city:
            return Response({"error": "City is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch weather data
        weather_response = get_weather(city, request_code)
        if weather_response.status_code != 200:
            return Response({"error": "Error fetching weather data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        weather_data = weather_response.json()
        temperature = float_temperature(weather_data)

        # Fetch playlist based on temperature
        playlist_response = get_playlist(temperature, request_code)
        if playlist_response.status_code != 200:
            return Response({"error": "Error fetching playlist data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        playlist_data = playlist_response.json()

        return Response(playlist_data, status=status.HTTP_200_OK)
