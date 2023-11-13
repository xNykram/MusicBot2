from app.core.sc.search import sc_search
from app.core.yt.search import yt_search
from app.schemas.song import Song


def search(query: str) -> Song:
    if "https://soundcloud.com/" in query:
        song = sc_search(query)
    else:
        song = yt_search(query)
    return song
