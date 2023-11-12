import platform

import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Help(commands.Cog):
    def __init__(self, client: Bot):
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


async def setup(client: Bot) -> None:
    await client.add_cog(Help(client))
