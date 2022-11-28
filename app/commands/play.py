from logging import Logger
from youtube_search import YoutubeSearch as SearchEngine
from ast import literal_eval
from discord.ext.commands.context import Context
from main import client

logger = Logger("play")

def on_downloaded(_: str):
    pass

def search(query: str) -> dict:
    result = SearchEngine(query, max_results=1).videos
    print(result[0].__str__())
    if len(result) == 0:
        return {}

    return literal_eval(result[0].__str__()) # Converts str to dict.


YDL_OPTS = {
    'format': 'm4a/bestaudio/best',
    'quiet': True,
    'audioonly': True,
    'outtmpl': '-',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
    'post_hooks': [on_downloaded],
}

@client.command(name="play")
async def play(ctx: Context, *, query: str):
    """Play a song from YouTube"""
    logger.info("Searching for song...")
    result = search(query)
    if result == {}:
        return await ctx.send("No result found.")

    if ctx.guild is None:
        return await ctx.send("You must be in a guild to use this command.")

    queue = client.get_queue(ctx.guild.id)
    queue.append({"title": result["title"], "url": f'youtube.com{result["url_suffix"]}', "duration": result["duration"]})
    song = queue.pop()
    await ctx.send(f"Playing {song['title']} ({song['duration']}) ({song['url']})")

    if ctx.guild.voice_client is None:
        return
    else:
        vc = await ctx.guild.voice_client.connect(timeout=10, reconnect=True)
    # play a song from the queue 



async def setup(bot):
    bot.add_command(play)
    logger.info("Setup done.")
