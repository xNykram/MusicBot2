from discord.ext.commands.context import Context
from app.main import client
from app.api.player import play_song
from app.api.search import yt_search


@client.command(name="play")
async def play(ctx: Context, *, query=None):
    if not ctx.message.author.voice:
        return await ctx.send("You are not on any voice channel.")
    if not query:
        return await ctx.send(
            "Please specify a song name or url.\n**Example**: !play Best EDM Music",
        )
    voice_client = await ctx.invoke(client.get_command("join"))
    queue = client.get_queue(ctx.guild.id)
    new_song = yt_search(query)

    if not new_song:
        return await ctx.send("No result found.")

    if ctx.guild is None:
        return await ctx.send("You must be in a guild to use this command.")

    if voice_client.is_playing():
        queue.append(new_song)
        await ctx.send("Added {} to queue!".format(new_song.name))

    else:
        await ctx.send(
            "Playing {} ({}) ({})".format(
                new_song.name,
                new_song.url,
                new_song.duration,
            ),
        )
        play_song(guild_id=ctx.guild.id, voice=voice_client, song_url=new_song.url)


async def setup(bot):
    bot.add_command(play)
