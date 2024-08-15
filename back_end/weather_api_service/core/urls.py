from django.urls import path

from core.views import WeatherAPIVIEW

urlpatterns = [
    # Outros caminhos
    path("weather/", WeatherAPIVIEW.as_view(), name="weather-api"),
]
