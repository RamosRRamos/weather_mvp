from rest_framework import serializers
from .models import SearchWeather, ResultWeather

class SearchWeatherSerializer(serializers.ModelSerializer):
    """
    Serializer for the SearchWeather model.

    This serializer handles the serialization and deserialization of SearchWeather objects,
    including the following fields:
        - id: The unique identifier of the search.
        - city: The name of the city for which the weather was searched.
        - request_id: A unique identifier for the weather search request.
    """
    class Meta:
        model = SearchWeather
        fields = ["id", "city", "request_id"]

class ResultWeatherSerializer(serializers.ModelSerializer):
    """
    Serializer for the ResultWeather model.

    This serializer handles the serialization and deserialization of ResultWeather objects,
    including the following fields:
        - id: The unique identifier of the weather result.
        - search: The SearchWeather instance associated with this result.
        - playlist_data: The JSON data containing the playlist information.
        - wheater_data: The JSON data containing the weather information.
        - temperature: The current temperature extracted from the weather data (read-only).
        - playlist: The playlist extracted from the playlist data (read-only).
    """

    temperature = serializers.ReadOnlyField()
    playlist = serializers.ReadOnlyField()

    class Meta:
        model = ResultWeather
        fields = [
            "id",
            "search",
            "playlist_data",
            "wheater_data",
            "temperature",
            "playlist",
        ]

    def to_representation(self, instance):
        """
        Customizes the serialized representation of the ResultWeather instance.

        Adds the 'city' field from the related SearchWeather instance to the serialized output.

        Args:
            instance (ResultWeather): The ResultWeather instance being serialized.

        Returns:
            dict: The customized serialized representation of the instance.
        """
        representation = super().to_representation(instance)
        representation["city"] = instance.search.city
        return representation
