from discord.ext import commands
from discord.ext.commands import Bot

from app.core.player import mp


class Clear(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.command(help="Clears the current queue of songs.")
    async def clear(self, ctx: commands.Context):
        queue_list = mp.return_queue(ctx.guild.id)
        if queue_list:
            mp.queue.clear()
            return await ctx.channel.send("The queue has been cleared.")
        return await ctx.channel.send("There is nothing to clear.")


async def setup(client: Bot) -> None:
    await client.add_cog(Clear(client))
