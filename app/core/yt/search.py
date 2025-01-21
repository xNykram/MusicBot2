from ast import literal_eval
from app.core.utils import millis_converter
from ytsearch import YTSearch as SearchEngine

from app.schemas.song import Song


def yt_search(query: str) -> dict | int:
    search_engine = SearchEngine()
    if "https://" in query:
        result = search_engine.search_by_url(query)
        result.update({'duration': millis_converter(int(result.get('duration')))})
    else:
        result = search_engine.search_by_term(query, max_results=1)
    if len(result) == 0:
        return 0
    result = result[0]
    target_song = Song(
        id=result.get('id'),
        name=result.get("title"),
        duration=result.get("duration"),
        url="https://www.youtube.com/watch?v=" + result.get("id"),
    )
    return target_song