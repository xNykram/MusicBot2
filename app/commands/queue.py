from logging import Logger
from app.main import client

logger = Logger("queue")


@client.command(name="queue")
async def queue(ctx):
    queue_list = client.get_queue(ctx.guild.id)
    if queue_list:
        buffer = ""
        for song in queue_list:
            buffer += "{}. {}\n".format(song.id, song.name)
        return await ctx.channel.send("**Current queue:**\n" "{}".format(buffer))
    return await ctx.channel.send("Queue is empty!")


async def setup(bot):
    bot.add_command(queue)
    logger.info("Setup done.")
