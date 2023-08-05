from app.core.player import play_song
from app.main import client


@client.command(name="skip", description="Skips the currently playing song.")
async def skip(ctx):
    queue = client.get_queue(ctx.guild.id)
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing() and not queue:
        voice_client.stop()
        await ctx.channel.send("Stopped playing the current song.")
    elif queue:
        voice_client.stop()
        next_song = queue[0]
        play_song(guild_id=ctx.guild.id, voice=voice_client)
        await ctx.channel.send(f"Now playing {next_song.name}")
    else:
        await ctx.channel.send("There is nothing to skip!")


async def setup(bot):
    bot.add_command(skip)
