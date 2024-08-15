from rest_framework import serializers
from .models import OpenAIRequest, LogOpenAIRequest


class OpenAIRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenAIRequest
        fields = [
            "id",
            "prompt",
            "created_at",
            "updated_at",
        ]  # Incluindo campos de controle de tempo, caso existam em AbstractBaseModel


class LogOpenAIRequestSerializer(serializers.ModelSerializer):
    data_hash = serializers.CharField(
        read_only=True
    )  # Hash é gerado automaticamente no modelo
    request_code = serializers.UUIDField(
        read_only=True
    )  # Se request_code for gerado no modelo ou automaticamente

    class Meta:
        model = LogOpenAIRequest
        fields = [
            "id",
            "request",
            "data",
            "data_hash",
            "request_code",
            "created_at",
            "updated_at",
        ]  # Incluindo campos de controle de tempo, caso existam em AbstractBaseModel
