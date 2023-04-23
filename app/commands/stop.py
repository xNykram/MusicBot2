from app.main import client


@client.command(
    name="stop", description="Stops playing the current song and clears the queue."
)
async def stop(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.channel.send("Stopped playing the current song.")
    else:
        await ctx.channel.send("There are no more songs in the queue.")


async def setup(bot):
    bot.add_command(stop)
