import json
import re

import requests
from bs4 import BeautifulSoup

from app.core.utils import millis_converter
from app.schemas.song import Song


def sc_search(query: str) -> dict | int:
    data = requests.get(query, timeout=30)
    sc_page = BeautifulSoup(data.content, features="html5lib")
    song_title = sc_page.find("h1")
    if not song_title:
        return 0
    song_title = song_title.text.replace("\n", " ")
    song_duration = sc_page.find_all("div", {"class": "sc-visuallyhidden"})
    script_tag = sc_page.find_all("script")
    script_tag = re.findall(r'"full_duration":[0-9]+', str(script_tag))[0]
    song_duration = json.loads("{" + script_tag + "}")
    song_duration_min = millis_converter(song_duration["full_duration"])
    return Song(id=query, name=song_title, url=query, duration=song_duration_min)
