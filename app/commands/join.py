from app.main import client
from logging import Logger

logger = Logger("join")

connections = {}


@client.command(name="join")
async def join(ctx):
    channnel = ctx.message.author.voice

    if not channnel:
        return await ctx.send("You are not on any voice channel.")
    if ctx.guild.id not in connections:
        await ctx.guild.change_voice_state(channel=ctx.author.voice.channel)
        connections.update({ctx.guild.id: ctx.author.voice.channel.id})
    else:
        return await ctx.send("I'm already connected to your voice channel.")


async def setup(bot):
    bot.add_command(join)
    logger.info("Setup done.")
