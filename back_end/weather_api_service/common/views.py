from rest_framework.response import Response
from rest_framework.views import APIView

from common.snippets import get_weather


class WeatherAPIVIEW(APIView):
    def get(self, request):
        city = request.query_params.get("city")
        response = get_weather(city)
        return Response(response.json())
