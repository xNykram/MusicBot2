from logging import Logger
from app.main import client
from app.api.player import Player

logger = Logger("skip")


@client.command(name="skip")
async def skip(ctx):
    queue = client.get_queue(ctx.guild.id)
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.channel.send("Stopped playing the current song.")
    if queue:
        next_song = queue.popleft()
        Player(
            guild_id=ctx.guild.id, song_url=next_song.url, voice_connection=voice_client
        )
        await ctx.channel.send("Now playing {}".format(next_song.name))


async def setup(bot):
    bot.add_command(skip)
    logger.info("Setup done.")
