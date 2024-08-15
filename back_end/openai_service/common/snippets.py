from decouple import config
from openai import OpenAI


def chat_gpt(prompt):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=config("OPENAI_API_KEY"),
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return response


def get_playlist(genre, amount=10, youtube_link=True):
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
