import discord
from discord.ext import commands
from app.main import client


@client.command(pass_context=True)
async def help(ctx):
    info = ["** !" + command.name + "** - " + command.description + " \n" for command in client.commands if not command.name == 'help']
    embed=discord.Embed(title="Available commands:", description=''.join(info), color=0x716d6d)
    embed.set_footer(text="Author: Nykram \nReport a bug: https://github.com/xNykram/music_bot/issues")
    await ctx.send(embed=embed)
    
    
async def setup(bot):
    bot.add_command(help)
