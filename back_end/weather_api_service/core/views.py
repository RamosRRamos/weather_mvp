# api/views.py
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import save_weather_data
from common.snippets import get_weather
import uuid


class WeatherAPIVIEW(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        city = request.query_params.get("city")
        response = get_weather(city)
        temperature = response.json().get("current", {}).get("temp_c", None)

        if temperature is not None:
            # Gera um UUID para o request_code
            request_code = uuid.UUID(request.query_params.get("request_code"))

            # Chama a tarefa Celery para salvar os dados
            save_weather_data.delay(city, temperature, response.json(), request_code)

        return Response(response.json())
