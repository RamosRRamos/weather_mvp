import pytest
from unittest.mock import patch, Mock
import openai

from common.snippets import chat_gpt

def test_openai_connection():
    """
    Tests if the connection to the OpenAI API is made correctly using the configured API key.

    Workflow:
        1. A test prompt is defined to simulate a request to the OpenAI API.
        2. The `chat_gpt` function is called with the test prompt.
        3. The response from the API is checked to ensure it matches the expected output.

    Asserts:
        - The API response content should be "This is a test." when trimmed of leading/trailing whitespace.
    """
    # Define a test prompt
    prompt = (
        "Test prompt for OpenAI API: Response from OpenAI is equal a 'This is a test.'."
    )

    response = chat_gpt(prompt)

    # Verify if the API response is correct
    assert response.choices[0].message.content.strip() == "This is a test."
