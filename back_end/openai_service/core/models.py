import hashlib
import json

from django.db import models

from common.models import AbstractBaseModel

class OpenAIRequest(AbstractBaseModel):
    """
    Model representing a request made to the OpenAI API.

    Attributes:
        prompt (str): The text prompt that was sent to the OpenAI API.
    """

    prompt = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the OpenAIRequest instance, which is the prompt text.

        Returns:
            str: The prompt text.
        """
        return self.prompt

class LogOpenAIRequest(AbstractBaseModel):
    """
    Model for logging the response from an OpenAI API request.

    Attributes:
        request (OpenAIRequest): A foreign key linking to the related OpenAIRequest instance.
        data (dict): The JSON data returned by the OpenAI API.
        data_hash (str): A SHA-256 hash of the JSON data for integrity verification.
        request_code (UUID): A unique code identifying the request.

    Methods:
        save: Overrides the default save method to automatically generate and store a SHA-256 hash of the JSON data.
    """

    request = models.ForeignKey(OpenAIRequest, on_delete=models.PROTECT)
    data = models.JSONField()
    data_hash = models.CharField(max_length=64, unique=True, editable=False)
    request_code = models.UUIDField()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to compute a SHA-256 hash of the JSON data before saving.

        The hash is stored in the data_hash field and ensures the integrity of the logged data.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        json_string = json.dumps(self.data, sort_keys=True)
        self.data_hash = hashlib.sha256(json_string.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the LogOpenAIRequest instance, which is the JSON data.

        Returns:
            str: The JSON data as a string.
        """
        return str(self.data)
