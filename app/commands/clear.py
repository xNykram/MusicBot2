from app.main import client


@client.command(name="clear")
async def clear(ctx):
    queue_list = client.get_queue(ctx.guild.id)
    if queue_list:
        client.queue_map.clear()
        return await ctx.channel.send("The queue has been cleared.")
    return await ctx.channel.send("There is nothing to clear.")


async def setup(bot):
    bot.add_command(clear)
