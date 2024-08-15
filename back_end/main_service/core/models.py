import uuid
from django.db import models
from common.models import AbstractBaseModel

class SearchWeather(AbstractBaseModel):
    """
    Represents a weather search request.

    Attributes:
        city (str): The name of the city for which the weather is being searched.
        request_id (UUID): A unique identifier for the request, automatically generated.
    """
    city = models.CharField(max_length=100)
    request_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        """
        Returns the string representation of the SearchWeather instance, which is the city name.

        Returns:
            str: The name of the city.
        """
        return self.city

class ResultWeather(AbstractBaseModel):
    """
    Represents the weather result associated with a specific search.

    Attributes:
        search (SearchWeather): The search instance to which this result is related.
        playlist_data (dict): The JSON data containing the playlist information returned from the playlist service.
        weather_data (dict): The JSON data containing the weather information returned from the weather service.
    """

    search = models.ForeignKey(SearchWeather, on_delete=models.CASCADE)
    playlist_data = models.JSONField()
    wheater_data = models.JSONField()

    @property
    def temperature(self):
        """
        Returns the current temperature in Celsius from the weather data.

        Returns:
            float: The current temperature in Celsius.
        """
        return float(self.wheater_data["current"]["temp_c"])

    @property
    def playlist(self):
        """
        Returns the playlist suggested by the GPT response from the playlist data.

        Returns:
            list: The playlist generated by the GPT model.
        """
        return self.playlist_data["response_gpt"]

    def __str__(self):
        """
        Returns the string representation of the ResultWeather instance, which includes the city name
        and the current temperature.

        Returns:
            str: A string in the format 'City Name - Temperature°C'.
        """
        return f"{self.search.city} - {self.temperature}°C"
