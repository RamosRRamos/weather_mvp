from requests.models import Response
from unittest.mock import patch, Mock

from common.snippets import get_weather


@patch("requests.get")
def test_get_weather(mock_get):
    # Configurar a resposta simulada
    mock_response = Mock(spec=Response)
    expected_data = {"location": {"name": "London"}, "current": {"temp_c": 20}}
    mock_response.json.return_value = expected_data
    mock_get.return_value = mock_response

    # Chamar a função
    city = "London"
    response = get_weather(city)
    # Verificar se a resposta está correta
    assert response.json() == expected_data
