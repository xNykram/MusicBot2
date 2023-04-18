from app.main import client


@client.command(name="join")
async def join(ctx):
    channel = ctx.author.voice
    if channel:
        if ctx.guild.voice_client is not None:
            await ctx.guild.voice_client.move_to(channel.channel)
        else:
            await channel.channel.connect()
    else:
        await ctx.channel.send("You are not connected to a voice channel.")

    return ctx.guild.voice_client


async def setup(bot):
    bot.add_command(join)
