import logging
import yt_dlp
from discord import VoiceClient, FFmpegPCMAudio
from app.main import client
from app.schemas.error import ErrorResponse

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


class Player:
    def __init__(self, guild_id: int, voice_connection: VoiceClient, song_url: str):
        self.guild_id = guild_id
        self.voice_connection = voice_connection
        self.song_stout = None
        self.song_url = song_url

    async def play_song(self, voice):
        try:
            song_stream = self.download_song(self.song_url)

            voice.play(
                FFmpegPCMAudio(song_stream["source"], **FFMPEG_OPTIONS),
                after=lambda _: self.play_next(voice),
            )
        except Exception as key:
            logging.warning(key)
            return ErrorResponse(type="YTDL", data=str(key))

    def play_next(self, voice):
        queue = client.get_queue(self.guild_id)
        if not len(queue) == 0:
            queue.pop(0)
        if len(queue) > 0:
            song_stream = self.download_song(queue[0].url)
            voice.play(
                FFmpegPCMAudio(song_stream["source"], **FFMPEG_OPTIONS),
                after=lambda _: self.play_next(voice),
            )
        else:
            logging.warning("Queue is empty.")

    @staticmethod
    def try_again(ydl, song_url):
        for _ in range(3):
            info = ydl.extract_info("ytsearch:%s" % song_url, download=False)
            print(info)
            if len(info["entries"]) > 0:
                return info
        return 1

    def download_song(self, song_url):
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.cache.remove()
            info = ydl.extract_info("ytsearch:%s" % song_url, download=False)
            entries_len = len(info["entries"])
            if entries_len == 0:
                info = self.try_again(ydl, song_url)
                if info == 1:
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
