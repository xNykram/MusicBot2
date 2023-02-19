from logging import Logger
from app.main import client

logger = Logger("leave")


@client.command(name="leave")
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
    logger.info("Setup done.")
