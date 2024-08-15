import pytest

from common.snippets import get_playlist


# Supondo que a função get_pop_playlist esteja em um arquivo chamado playlist.py


def test_get_pop_playlist_default():
    result = get_playlist(gender='pop')

    # Verifique se o resultado contém 10 músicas
    playlist = result.splitlines()
    assert len(playlist) == 10

    # Verifique se cada linha segue o formato "Nome da Musica; Artista; link"
    for line in playlist:
        parts = line.split(';')
        assert len(parts) == 3  # Nome da Musica, Artista, Link
        assert "https://" in parts[2].strip()  # Verifica se o link parece um link válido


def test_get_pop_playlist_no_youtube_links():
    result = get_playlist(gender='pop', youtube_link=False)

    # Verifique se o resultado contém 10 músicas
    playlist = result.splitlines()
    assert len(playlist) == 10

    # Verifique se cada linha segue o formato "Nome da Musica; Artista;"
    for line in playlist:
        parts = line.split(';')
        assert len(parts) == 2  # Nome da Musica, Artista
        assert parts[1].strip() != ''  # Verifica se o Artista não está vazio


if __name__ == "__main__":
    pytest.main()
