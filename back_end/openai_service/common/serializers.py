"""
Module: serializers
Serializers for data validation and serialization.
"""

from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    """
    Serializer to validate and serialize a message.
    """

    message = serializers.CharField()
