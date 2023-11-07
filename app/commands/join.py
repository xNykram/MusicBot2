from discord.ext import commands


class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help="Joins the voice channel that the user is in.")
    async def join(self, ctx: commands.Context):
        channel = ctx.author.voice
        if channel:
            if ctx.guild.voice_client is not None:
                await ctx.guild.voice_client.move_to(channel.channel)
            else:
                await channel.channel.connect()
        else:
            await ctx.channel.send("You are not connected to a voice channel.")

        return ctx.guild.voice_client


async def setup(client):
    await client.add_cog(Join(client))
