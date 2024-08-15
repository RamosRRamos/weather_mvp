import uuid

from django.db import models

from common.models import AbstractBaseModel


class SearchWeather(AbstractBaseModel):
    city = models.CharField(max_length=100)
    request_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.city


class ResultWeather(AbstractBaseModel):
    search = models.ForeignKey(SearchWeather, on_delete=models.CASCADE)

    playlist_data = models.JSONField()
    wheater_data = models.JSONField()

    @property
    def temperature(self):
        return float(self.wheater_data["current"]["temp_c"])

    @property
    def playlist(self):
        return self.playlist_data["response_gpt"]

    def __str__(self):
        return f"{self.search.city} - {self.temperature}°C"
