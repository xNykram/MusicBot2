from app.main import client


@client.command(name="queue", description="Shows the current queue of songs.")
async def queue(ctx):
    queue_list = client.get_queue(ctx.guild.id)

    if queue_list:
        buffer = ""
        for index, song in enumerate(queue_list):
            buffer += f"{index + 1}. {song.name}\n"
        return await ctx.channel.send(f"**Current queue:**\n {buffer}")
    return await ctx.channel.send("Queue is empty!")


async def setup(bot):
    bot.add_command(queue)
