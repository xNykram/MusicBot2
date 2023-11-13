import pytest

from app.core import search as search_module
from app.core.utils import millis_converter
from app.schemas.song import Song


def test_millis_converter():
    response = millis_converter(123456)

    assert isinstance(response, str)
    assert response == "2:03"


@pytest.mark.parametrize(
    "video_url", [("https://youtube.com/test_vide_id"), ("https://soundcloud.com/test_vide_id")]
)
def test_search_yt(monkeypatch, video_url):
    fake_song = Song(
        id="123", name="TestSong", url="https://fake_url.com/test_url", duration="1:00"
    )

    def mock_yt_search_response(song):
        return fake_song

    def mock_sc_search_response(song):
        return fake_song

    monkeypatch.setattr(search_module, "yt_search", mock_yt_search_response)
    monkeypatch.setattr(search_module, "sc_search", mock_sc_search_response)

    response = search_module.search(video_url)

    assert isinstance(response, Song)
    assert response.id == fake_song.id
    assert response.name == fake_song.name
    assert response.url == fake_song.url
    assert response.duration == fake_song.duration
