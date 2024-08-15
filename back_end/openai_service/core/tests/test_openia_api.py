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
