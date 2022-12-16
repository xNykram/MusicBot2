from app.main import client
from logging import Logger
from app.commands.join import connections

logger = Logger("leave")


@client.command(name="leave")
async def leave(ctx):
    channnel = ctx.message.author.voice

    if channnel:
        if ctx.guild.id not in connections:
            return await ctx.send("I'm not connected to your voice channel.")
        else:
            del connections[ctx.guild.id]
            return await ctx.guild.change_voice_state(channel=None)
    else:
        return await ctx.send("You have to be in a voice channel to do that.")


async def setup(bot):
    bot.add_command(leave)
    logger.info("Setup done.")
