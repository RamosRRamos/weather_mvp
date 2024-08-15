from decouple import config
from openai import OpenAI

def chat_gpt(prompt):
    """
    Sends a prompt to the OpenAI GPT model and returns the response.

    Args:
        prompt (str): The prompt to send to the GPT model.

    Returns:
        response: The response object from the GPT model, containing the generated content.
    """
    client = OpenAI(
        # This is the default and can be omitted
        api_key=config("OPENAI_API_KEY"),
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return response

def get_playlist(genre, amount=10, youtube_link=True):
    """
    Generates a music playlist using the GPT model based on the specified genre.

    Args:
        genre (str): The genre of music for the playlist (e.g., "pop", "rock").
        amount (int): The number of songs to include in the playlist. Default is 10.
        youtube_link (bool): Whether to include YouTube links in the playlist. Default is True.

    Returns:
        dict: A dictionary containing the prompt used and the GPT-generated playlist.
            - "prompt": The full prompt sent to the GPT model.
            - "response_gpt": A list of strings where each string represents a line in the playlist, formatted as "Song Name; Artist; [Link]".
    """
    start_prompt = f"gere uma playlist {genre}"
    youtube_prompt = "com links do youtube" if youtube_link else ""
    youtube_format = "link" if youtube_link else ""
    request_format_prompt = (
        f"formato de saida: Nome da Musica; Artista; {youtube_format}"
    )
    end_prompt = f"Nada mais além disso; {amount} musicas na playlist."

    prompt = f"{start_prompt} {youtube_prompt}, {request_format_prompt} {end_prompt}."

    response_gpt = chat_gpt(prompt)

    response = {
        "prompt": prompt,
        "response_gpt": response_gpt.choices[0].message.content.split('\n'),
    }

    return response
