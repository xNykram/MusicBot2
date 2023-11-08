from discord.ext import commands
from app.core.player import mp, play_song
from app.core.search import search


class Play(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(
        help="Plays a song or adds it to the queue if a song is already playing."
    )
    async def play(self, ctx: commands.Context, *, query=None):
        if not ctx.message.author.voice:
            return await ctx.send("You are not on any voice channel.")
        if not query:
            return await ctx.send(
                "Please specify a song name or url.\n**Example**: !play Best EDM Music",
            )
        voice_client = await ctx.invoke(self.client.get_command("join"))
        queue = mp.return_queue(ctx.guild.id)
        new_song = search(query)

        if not new_song:
            return await ctx.send("No result found.")

        if ctx.guild is None:
            return await ctx.send("You must be in a guild to use this command.")

        if voice_client.is_playing():
            queue.append(new_song)
            await ctx.send(f"Added {new_song.name} to queue!")

        else:
            await ctx.send(
                f"Playing {new_song.name} ({new_song.url}) ({new_song.duration})"
            )
            queue.append(new_song)
            play_song(guild_id=ctx.guild.id, voice=voice_client)


async def setup(client):
    await client.add_cog(Play(client))
