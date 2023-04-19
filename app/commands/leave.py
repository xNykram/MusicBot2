from app.main import client


@client.command(name="leave", description="Leaves the voice channel.")
async def leave(ctx):
    channel = ctx.author.voice
    if channel:
        if ctx.guild.voice_client is not None:
            await ctx.guild.voice_client.disconnect()
            client.queue_map.clear()
    else:
        await ctx.channel.send("You are not connected to a voice channel.")


async def setup(bot):
    bot.add_command(leave)
