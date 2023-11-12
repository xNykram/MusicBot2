from app.core.yt import search
from app.schemas.song import Song


class MockSearchEngine:
    def __init__(self, query, max_results):
        self.videos = [{"id": "video_id", "title": "Video Title", "duration": "5:30"}]


class MockSearchEngineNoVideos:
    def __init__(self, query, max_results):
        self.videos = []


def test_yt_search_valid_song(monkeypatch):
    mockSE = MockSearchEngine("Some Music", 1)
    monkeypatch.setattr(search, "SearchEngine", MockSearchEngine)

    result = search.yt_search("Some Music")

    assert isinstance(result, Song)
    assert result.id == mockSE.videos[0]["id"]
    assert result.name == mockSE.videos[0]["title"]
    assert result.duration == mockSE.videos[0]["duration"]
    assert result.url == "https://www.youtube.com/watch?v=" + mockSE.videos[0]["id"]


def test_yt_search_no_song(monkeypatch):
    monkeypatch.setattr(search, "SearchEngine", MockSearchEngineNoVideos)

    result = search.yt_search("Some Music")

    assert result == 0
