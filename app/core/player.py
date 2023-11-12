import yt_dlp
from discord import FFmpegPCMAudio, PCMVolumeTransformer, VoiceClient

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


class MusicPlayer:
    def __init__(self) -> None:
        self.queue = {}

    def return_queue(self, guild_id: str) -> list:
        if guild_id not in self.queue:
            self.queue[guild_id] = []
        return self.queue.get(guild_id, [])


mp = MusicPlayer()


def play_song(guild_id: str, voice: VoiceClient):
    queue = mp.return_queue(guild_id)
    if len(queue) > 0:
        song_url = queue[0].url
        queue.pop(0)
        song_stream = download_song(song_url)
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
            error = (
                f"Could not download requested song, please try again later. Song url: {song_url}"
            )
            raise IndexError(error)
        info = info["entries"][0]
        audio = next(
            f
            for f in info["formats"]
            if ("acodec" in f and (f["acodec"] != "none" and f["vcodec"] == "none"))
        )
    return {"source": audio["url"], "title": info["title"]}
