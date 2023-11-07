import discord
import platform

from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx: commands.Context):
        available_commands = [
            f"**!{command.name}** - {command.help or 'No description available'}\n"
            for command in self.client.commands
            if not command.name == "help"
        ]

        embed = discord.Embed(
            title="Available commands:",
            description="".join(available_commands),
            color=0x716D6D,
        )
        embed.set_footer(text=f"Author: Nykram | Python: {platform.python_version()}")
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Help(client))
