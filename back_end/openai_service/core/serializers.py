from rest_framework import serializers
from .models import OpenAIRequest, LogOpenAIRequest

class OpenAIRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for the OpenAIRequest model.

    This serializer handles the serialization and deserialization of OpenAIRequest objects,
    including the following fields:
        - id: The unique identifier of the OpenAI request.
        - prompt: The prompt sent to the OpenAI API.
        - created_at: The timestamp of when the request was created.
        - updated_at: The timestamp of when the request was last updated.

    Meta:
        - model: Specifies the model being serialized (OpenAIRequest).
        - fields: Lists the fields to be included in the serialized output.
    """
    class Meta:
        model = OpenAIRequest
        fields = [
            "id",
            "prompt",
            "created_at",
            "updated_at",
        ]

class LogOpenAIRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for the LogOpenAIRequest model.

    This serializer handles the serialization and deserialization of LogOpenAIRequest objects,
    including the following fields:
        - id: The unique identifier of the log entry.
        - request: The related OpenAIRequest instance.
        - data: The JSON data containing the GPT response.
        - data_hash: A read-only field that stores a hash of the data for verification purposes.
        - request_code: A read-only UUID that uniquely identifies the request.
        - created_at: The timestamp of when the log entry was created.
        - updated_at: The timestamp of when the log entry was last updated.

    Meta:
        - model: Specifies the model being serialized (LogOpenAIRequest).
        - fields: Lists the fields to be included in the serialized output.
    """
    data_hash = serializers.CharField(
        read_only=True
    )
    request_code = serializers.UUIDField(
        read_only=True
    )

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
        ]
