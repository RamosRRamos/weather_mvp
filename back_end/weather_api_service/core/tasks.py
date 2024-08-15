# api/tasks.py
from celery import shared_task
from .models import ConsultWeather, LogConsultWhather
import json
import hashlib


@shared_task
def save_weather_data(city, temperature, data, request_code):
    # Salvar a consulta principal
    consult = ConsultWeather.objects.create(city=city, temperature=temperature)

    # Gerar o hash dos dados JSON
    json_string = json.dumps(data, sort_keys=True)
    data_hash = hashlib.sha256(json_string.encode()).hexdigest()

    # Salvar o log da consulta
    LogConsultWhather.objects.create(
        consult=consult, data=data, data_hash=data_hash, request_code=request_code
    )
