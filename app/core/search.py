from ast import literal_eval
from youtube_search import YoutubeSearch as SearchEngine
from app.schemas.song import Song


def yt_search(query: str) -> dict:
    result = SearchEngine(query, max_results=1).videos
    if len(result) == 0:
        return 0
    video = literal_eval(str(result[0]))
    return Song(
        id=video["id"],
        name=video["title"],
        duration=video["duration"],
        url="https://www.youtube.com/watch?v=" + video["id"],
    )
