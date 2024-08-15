from rest_framework import serializers
from .models import SearchWeather, ResultWeather


class SearchWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchWeather
        fields = ["id", "city", "request_id"]


class ResultWeatherSerializer(serializers.ModelSerializer):
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
        representation = super().to_representation(instance)
        representation["city"] = instance.search.city
        return representation
