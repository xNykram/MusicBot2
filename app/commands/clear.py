from discord.ext import commands
from app.core.player import mp


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(help="Clears the current queue of songs.")
    async def clear(self, ctx: commands.Context):
        queue_list = mp.return_queue(ctx.guild.id)
        if queue_list:
            mp.queue_map.clear()
            return await ctx.channel.send("The queue has been cleared.")
        return await ctx.channel.send("There is nothing to clear.")


async def setup(client):
    await client.add_cog(Clear(client))
