from app.main import client


@client.command(name="volume", description="Changes the volume of the bot.")
async def volume(ctx, vol: int):
    voice_client = ctx.guild.voice_client
    if 1 <= vol <= 100:
        if voice_client.is_playing():
            new_volume = vol / 100
            voice_client.source.volume = new_volume
        else:
            await ctx.channel.send("Bot is not playing any songs.")
    else:
        await ctx.channel.send("The volume number must be between 1 - 100")


async def setup(bot):
    bot.add_command(volume)
