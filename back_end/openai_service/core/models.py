import hashlib
import json

from django.db import models

from common.models import AbstractBaseModel


# Create your models here.
class OpenAIRequest(AbstractBaseModel):
    """
    OpenAIRequest model
    """

    prompt = models.TextField()

    def __str__(self):
        return self.prompt


class LogOpenAIRequest(AbstractBaseModel):
    """
    OpenAIRequest model
    """

    request = models.ForeignKey(OpenAIRequest, on_delete=models.PROTECT)
    data = models.JSONField()
    data_hash = models.CharField(max_length=64, unique=True, editable=False)
    request_code = models.UUIDField()

    def save(self, *args, **kwargs):
        json_string = json.dumps(self.data, sort_keys=True)
        self.data_hash = hashlib.sha256(json_string.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.data
