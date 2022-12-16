import logging

from discord import PCMVolumeTransformer, VoiceClient, FFmpegPCMAudio
from youtube_dl import YoutubeDL
from app.main import client

ydl_options = {'format': 'bestaudio', 'noplaylist': 'True'}

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

ytdl = YoutubeDL(ydl_options)


class Player:
    def __init__(self, guild_id: int, voice_connection: VoiceClient, song_url: str):
        self.guild_id = guild_id
        self.voice_connection = voice_connection
        self.song_stout = None
        self.song_url = song_url

    def download_song(self):
        with YoutubeDL(ydl_options) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % self.song_url, download=False)['entries'][0]
            except Exception as key:
                return logging.warning("Failed to download a song: {}".format(str(key)))
        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_song(self, voice):
        try:
            song_data = self.download_song()
            voice.play(FFmpegPCMAudio(song_data['source'], **FFMPEG_OPTIONS), after=lambda x: self.play_next(voice))
        except Exception as key:
            logging.warning(key)

    def play_next(self, voice):
        queue = client.get_queue(self.guild_id)
        if len(queue) > 0:
            song = queue.pop()
            self.song_url = song['url']
            song_data = self.download_song()
            # voice.play(FFmpegPCMAudio(song_data['source'], **FFMPEG_OPTIONS), after=lambda x: self.play_next())
        else:
            self.voice_connection.is_playing = False
