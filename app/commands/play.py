from discord.ext.commands.context import Context

from app.core.player import play_song
from app.core.search import search
from app.main import client


@client.command(
    name="play",
    description="Plays a song or adds it to the queue if a song is already playing.",
)
async def play(ctx: Context, *, query=None):
    if not ctx.message.author.voice:
        return await ctx.send("You are not on any voice channel.")
    if not query:
        return await ctx.send(
            "Please specify a song name or url.\n**Example**: !play Best EDM Music",
        )
    voice_client = await ctx.invoke(client.get_command("join"))
    queue = client.get_queue(ctx.guild.id)
    new_song = search(query)

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
        queue.append(new_song)
        play_song(guild_id=ctx.guild.id, voice=voice_client)


async def setup(bot):
    bot.add_command(play)
