from discord.ext import commands
from app.core.player import mp


class Leave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help="Leaves the voice channel.")
    async def leave(self, ctx: commands.Context):
        channel = ctx.author.voice
        if channel:
            if ctx.guild.voice_client is not None:
                await ctx.guild.voice_client.disconnect()
                mp.queue.clear()
        else:
            await ctx.channel.send("You are not connected to a voice channel.")


async def setup(client):
    await client.add_cog(Leave(client))
