import uuid

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.snippets import get_weather, float_temperature, get_playlist


# Create your views here.
class PlaylistView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        city = request.query_params.get("city")
        request_code = uuid.uuid4()

        if not city or not request_code:
            return Response({"error": "City and request_code are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Obter os dados do clima
        weather_response = get_weather(city, request_code)
        if weather_response.status_code != 200:
            return Response({"error": "Error fetching weather data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        weather_data = weather_response.json()
        temperature = float_temperature(weather_data)

        # Obter a playlist baseada na temperatura
        playlist_response = get_playlist(temperature, request_code)
        if playlist_response.status_code != 200:
            return Response({"error": "Error fetching playlist data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        playlist_data = playlist_response.json()

        return Response(playlist_data, status=status.HTTP_200_OK)
