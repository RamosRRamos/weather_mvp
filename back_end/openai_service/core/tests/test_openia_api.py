import pytest
from unittest.mock import patch, Mock
import openai

from common.snippets import chat_gpt


def test_openai_connection():
    """
    Testa se a conexão com a API da OpenAI é feita corretamente usando a chave de API configurada.
    """
    # Define um prompt de teste
    prompt = (
        "Test prompt for OpenAI API: Response from OpenAI is equal a 'This is a test.'."
    )

    response = chat_gpt(prompt)

    # Verifica se a resposta da API está correta
    assert response.choices[0].message.content.strip() == "This is a test."


def test_openai_missing_api_key():
    """
    Testa o comportamento da API OpenAI quando a chave da API está ausente.
    """
    # Remove a chave da API para este teste
    openai.api_key = None

    with pytest.raises(Exception) as excinfo:
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Test prompt"}],
            max_tokens=150,
        )

    # Verifica se o erro levantado é devido à ausência da chave da API
    assert "Authentication" in str(excinfo.value)


@patch("openai.ChatCompletion.create")
def test_openai_error_handling(mock_openai_create, mock_openai_api_key):
    """
    Testa o tratamento de erros ao se conectar à API da OpenAI.
    """
    # Simula um erro ao chamar a API
    mock_openai_create.side_effect = Exception("OpenAI API error")

    with pytest.raises(Exception) as excinfo:
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Test prompt"}],
            max_tokens=150,
        )

    # Verifica se o erro foi capturado corretamente
    assert "OpenAI API error" in str(excinfo.value)
