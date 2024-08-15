from rest_framework import serializers
from .models import ConsultWeather, LogConsultWhather


class ConsultWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultWeather
        fields = ["id", "city", "temperature"]


class LogConsultWhatherSerializer(serializers.ModelSerializer):
    consult = ConsultWeatherSerializer(
        read_only=True
    )  # Inclui os dados da consulta como leitura

    class Meta:
        model = LogConsultWhather
        fields = [
            "id",
            "consult",
            "data",
            "data_hash",
            "request_code",
        ]

    def create(self, validated_data):
        # Sobrescreve o create para associar a consulta corretamente
        consult_data = validated_data.pop("consult", None)
        if consult_data:
            consult = ConsultWeather.objects.create(**consult_data)
        else:
            consult = None
        log_consult = LogConsultWhather.objects.create(
            consult=consult, **validated_data
        )
        return log_consult
