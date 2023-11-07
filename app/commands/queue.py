from discord.ext import commands
from app.core.player import mp


class Queue(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help="Shows the current queue of songs.")
    async def queue(self, ctx: commands.Context):
        queue_list = mp.return_queue(ctx.guild.id)

        if queue_list:
            buffer = ""
            for index, song in enumerate(queue_list):
                buffer += f"{index + 1}. {song.name}\n"
            return await ctx.channel.send(f"**Current queue:**\n {buffer}")
        return await ctx.channel.send("Queue is empty!")


async def setup(client):
    await client.add_cog(Queue(client))
