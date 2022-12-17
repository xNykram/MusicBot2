from logging import Logger
from app.main import client
from app.commands.join import connections

logger = Logger("leave")


@client.command(name="leave")
async def leave(ctx):
    channel = ctx.message.author.voice
    if channel:
        current_connection = [
            connection
            for connection in connections
            if connection.guild_id == ctx.guild.id
        ]
        if (
            current_connection
            and current_connection[0].channel_id == ctx.author.voice.channel.id
        ):
            client.queue_map.clear()
            voice_client = current_connection[0].voice_client
            voice_client.stop()
            await voice_client.disconnect()
            connections.remove(current_connection[0])
            return await ctx.guild.change_voice_state(channel=None)

        return await ctx.send("I am not connected to your voice channel.")

    return await ctx.send("You have to be in a voice channel to do that.")


async def setup(bot):
    bot.add_command(leave)
    logger.info("Setup done.")
