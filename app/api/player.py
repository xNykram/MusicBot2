import yt_dlp
from app.main import client
from discord import VoiceClient, FFmpegPCMAudio

ydl_options = {
    "format": "bestaudio",
    "noplaylist": True,
    "youtube_include_dash_manifest": False,
    "default_search": "ytsearch",
}

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}


def play_song(guild_id: str, voice: VoiceClient, song_url: str):
    song_stream = download_song(song_url)
    try:
        voice.play(
            FFmpegPCMAudio(song_stream["source"], **FFMPEG_OPTIONS),
            after=lambda _: process_next_song(guild_id, voice),
        )
    except Exception:
        pass


def process_next_song(guild_id: str, voice: VoiceClient):
    queue = client.get_queue(guild_id)
    if not len(queue) == 0:
        queue.pop(0)
    if len(queue) > 0:
        try:
            song_stream = download_song(song=queue[-1].url)
            voice.play(
                FFmpegPCMAudio(song_stream["source"], **FFMPEG_OPTIONS),
                after=lambda _: process_next_song(voice),
            )
        except TypeError:
            pass


def download_song(song_url: str):
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.cache.remove()
        info = ydl.extract_info("ytsearch:%s" % song_url, download=False)
        entries_len = len(info["entries"])
        if entries_len == 0:
            raise Exception(
                "Could not download requested song, please try again later.",
            )
        info = info["entries"][0]
        audio = next(
            f
            for f in info["formats"]
            if (f["acodec"] != "none" and f["vcodec"] == "none")
        )
    return {"source": audio["url"], "title": info["title"]}
