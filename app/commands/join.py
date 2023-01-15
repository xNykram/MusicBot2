from uuid import uuid4
from logging import Logger
from app.main import client
from app.schemas.connections import Connections


logger = Logger("join")




@client.command(name="join")
async def join(ctx):
    channel = ctx.message.author.voice
    connections = client.connections

    if not channel:
        return await ctx.send("You are not on any voice channel.")

    current_connection = [
        connection for connection in connections if connection.guild_id == ctx.guild.id
    ]
    if current_connection:
        return current_connection[0].voice_client
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()
    connections.append(
        Connections(
            id=uuid4(),
            guild_id=ctx.guild.id,
            voice_client=voice_client,
            channel_id=ctx.author.voice.channel.id,
        )
    )
    return voice_client


async def setup(bot):
    bot.add_command(join)
    logger.info("Setup done.")
