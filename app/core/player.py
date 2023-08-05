import yt_dlp
from discord import FFmpegPCMAudio, PCMVolumeTransformer, VoiceClient

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
        queue.pop(0)
        audio_source = PCMVolumeTransformer(
            FFmpegPCMAudio(song_stream["source"], **FFMPEG_OPTIONS)
        )
        voice.play(audio_source, after=lambda _: play_song(guild_id, voice))


def download_song(song_url: str):
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.cache.remove()
        info = ydl.extract_info(f"ytsearch:{song_url}", download=False)
        entries_len = len(info["entries"])
        if entries_len == 0:
            raise IndexError(
                "Could not download requested song, please try again later.",
            )
        info = info["entries"][0]
        audio = next(
            f
            for f in info["formats"]
            if ("acodec" in f and (f["acodec"] != "none" and f["vcodec"] == "none"))
        )
    return {"source": audio["url"], "title": info["title"]}
