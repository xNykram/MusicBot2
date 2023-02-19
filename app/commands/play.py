from logging import Logger
from ast import literal_eval
from youtube_search import YoutubeSearch as SearchEngine
from discord.ext.commands.context import Context
from app.schemas.song import Song
from app.main import client
from app.api.player import Player
from app.schemas.error import ErrorResponse

logger = Logger("play")


def on_downloaded(_: str):
    pass


def search(query: str) -> dict:
    result = SearchEngine(query, max_results=1).videos
    if len(result) == 0:
        return {}

    return literal_eval(str(result[0]))


@client.command(name="play")
async def play(ctx: Context, *, query: str):
    """Play a song from YouTube"""
    if not ctx.message.author.voice:
        return await ctx.send("You are not on any voice channel.")
    voice_client = await ctx.invoke(client.get_command("join"))
    logger.info("Searching for song...")
    result = search(query)
    if result == {}:
        return await ctx.send("No result found.")

    if ctx.guild is None:
        return await ctx.send("You must be in a guild to use this command.")

    queue = client.get_queue(ctx.guild.id)
    current_song = Song(
        id=len(queue) + 1,
        name=result["title"],
        url="https://www.youtube.com" + result["url_suffix"],
        duration=result["duration"],
    )
    if len(queue) > 0:
        await ctx.send("Added {} to queue!".format(current_song.name))
        queue.append(current_song)
    else:
        queue.append(current_song)
        song = queue[-1]
        await ctx.send(
            "Playing {} ({}) ({})".format(song.name, song.url, song.duration)
        )
        player = Player(
            guild_id=ctx.guild.id, song_url=song.url, voice_connection=voice_client
        )
        response = await player.play_song(voice_client)
        if isinstance(response, ErrorResponse):
            client.queue_map.clear()
            return await ctx.send(
                "```Unable to download/play requested song! \nInfo: {}\nAll"
                " issues please report to the main developer: Nykram```".format(
                    response.data
                ).replace("https://", "")
            )


async def setup(bot):
    bot.add_command(play)
    logger.info("Setup done.")
