import yt_dlp
from discord import FFmpegPCMAudio, VoiceClient

from app.main import client

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


def play_song(guild_id: str, voice: VoiceClient):
    queue = client.get_queue(guild_id)
    if len(queue) > 0:
        song_url = queue[0].url
        song_stream = download_song(song_url)
        try:
            queue.pop(0)
            voice.play(
                FFmpegPCMAudio(song_stream["source"], **FFMPEG_OPTIONS),
                after=lambda _: play_song(guild_id, voice),
            )

        except Exception:
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
