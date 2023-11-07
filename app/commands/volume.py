# from app.main import client
from discord.ext import commands
from discord.utils import get
class Volume(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def volume(self, ctx, vol: int):
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if 1 <= vol <= 100:
            if voice.is_playing():
                new_volume = vol / 100
                voice.source.volume = new_volume
            else:
                await ctx.channel.send("Bot is not playing any songs.")
        else:
            await ctx.channel.send("The volume number must be between 1 - 100")

async def setup(client):
    await client.add_cog(Volume(client))