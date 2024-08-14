import hashlib
import json

from django.db import models

from common.models import AbstractBaseModel


class ConsultWeather(AbstractBaseModel):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"


class LogConsultWhather(AbstractBaseModel):
    consult = models.ForeignKey(ConsultWeather, on_delete=models.CASCADE)
    data = models.JSONField()
    data_hash = models.CharField(max_length=64, unique=True, editable=False)
    request_code = models.UUIDField()

    def save(self, *args, **kwargs):

        json_string = json.dumps(self.data, sort_keys=True)
        self.data_hash = hashlib.sha256(json_string.encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.consult.city} - {self.consult.temperature}°C"
