from app.core.sc.search import sc_search
from app.core.yt.search import yt_search


def search(query: str):
    if "https://soundcloud.com/" in query:
        song = sc_search(query)
    elif "https://open.spotify.com" in query:
        pass
    else:
        song = yt_search(query)
    return song
