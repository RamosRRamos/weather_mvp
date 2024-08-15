import requests
from decouple import config


def genre_to_playlist(temperature):
    if temperature > 25:
        return "pop"
    elif temperature >= 10:
        return "rock"
    else:
        return "classical"


def get_weather(city, request_code):
    base_url = config("WEATHER_SERVICE_URL")
    params = {
        "city": city,
        "request_code": request_code,
    }
    response = requests.get(base_url, params=params, timeout=30)
    return response


def get_playlist(temperature, request_code):
    genre = genre_to_playlist(temperature)
    base_url = config("PLAYLIST_SERVICE_URL")
    params = {
        "genre": genre,
        "amount": 10,
        "request_code": request_code,
    }
    response = requests.get(base_url, params=params, timeout=30)
    return response


def float_temperature(json_response):
    return float(json_response["current"]["temp_c"])


def playlist_data(json_response):
    return json_response["response_gpt"]
