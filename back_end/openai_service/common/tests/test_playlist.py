import pytest
from common.snippets import get_playlist

def test_get_pop_playlist_default():
    """
    Test the get_playlist function for the 'pop' genre with default settings.

    Steps:
        1. Call the get_playlist function with the 'pop' genre.
        2. Verify that the result contains exactly 10 songs.
        3. Check that each line of the playlist follows the format "Song Name; Artist; Link".
        4. Ensure that the link appears to be a valid URL (contains "https://").

    Asserts:
        - The playlist contains 10 songs.
        - Each song entry has three parts: Song Name, Artist, and Link.
        - The link part is a valid URL.
    """
    result = get_playlist(gender="pop")["response_gpt"]

    # Verify the result contains 10 songs
    playlist = result.splitlines()
    assert len(playlist) == 10

    # Verify each line follows the format "Song Name; Artist; Link"
    for line in playlist:
        parts = line.split(";")
        assert len(parts) == 3  # Song Name, Artist, Link
        assert (
            "https://" in parts[2].strip()
        )  # Check if the link appears to be a valid URL

def test_get_pop_playlist_no_youtube_links():
    """
    Test the get_playlist function for the 'pop' genre without YouTube links.

    Steps:
        1. Call the get_playlist function with the 'pop' genre and youtube_link set to False.
        2. Verify that the result contains exactly 10 songs.
        3. Check that each line of the playlist follows the format "Song Name; Artist;" without a link.

    Asserts:
        - The playlist contains 10 songs.
        - Each song entry has two parts: Song Name and Artist.
        - The Artist part is not empty.
    """
    result = get_playlist(gender="pop", youtube_link=False)["response_gpt"]

    # Verify the result contains 10 songs
    playlist = result.splitlines()
    assert len(playlist) == 10

    # Verify each line follows the format "Song Name; Artist;"
    for line in playlist:
        parts = line.split(";")
        assert len(parts) == 2  # Song Name, Artist
        assert parts[1].strip() != ""  # Ensure the Artist is not empty

if __name__ == "__main__":
    pytest.main()
