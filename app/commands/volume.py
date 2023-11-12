# from app.main import client
from discord.ext import commands
from discord.ext.commands import Bot


class Volume(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.command()
    async def volume(self, ctx, vol: int):
        voice_client = ctx.voice_client
        if voice_client:
            if 1 <= vol <= 100:
                if voice_client.is_playing():
                    new_volume = vol / 100
                    voice_client.source.volume = new_volume
                else:
                    await ctx.channel.send("Bot is not playing any songs.")
            else:
                await ctx.channel.send("The volume number must be between 1 - 100")
        else:
            await ctx.channel.send("I am not connected to any voice channels.")


async def setup(client: Bot) -> None:
    await client.add_cog(Volume(client))
