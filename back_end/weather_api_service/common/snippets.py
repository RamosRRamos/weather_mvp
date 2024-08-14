import requests
from decouple import config


def get_weather(city):
    api_key = config("API_KEY")  # Substitua pelo seu chave da WeatherAPI
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
    }
    response = requests.get(base_url, params=params, timeout=30)
    return response
