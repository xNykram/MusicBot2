import logging
from discord import VoiceClient, FFmpegPCMAudio
from youtube_dl import YoutubeDL
from app.main import client
from app.schemas.error import ErrorResponse

ydl_options = {"format": "bestaudio", "noplaylist": "True"}

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}

ytdl = YoutubeDL(ydl_options)


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
            song_stream = self.download_song(queue[-1].url)
            voice.play(
                FFmpegPCMAudio(song_stream["source"], **FFMPEG_OPTIONS),
                after=lambda _: self.play_next(voice),
            )
        else:
            logging.warning("Queue is empty.")

    @staticmethod
    def download_song(song_url):
        with YoutubeDL(ydl_options) as ydl:
            ydl.cache.remove()
            info = ydl.extract_info("ytsearch:%s" % song_url, download=False)[
                "entries"
            ][0]
        return {"source": info["formats"][0]["url"], "title": info["title"]}
