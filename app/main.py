import os
import logging
from os import listdir
from discord.ext import commands


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


client = Client(
    command_prefix=commands.when_mentioned_or(os.environ.get("PREFIX")),
    case_insensitive=True,
)


@client.event
async def on_ready():
    logging.warning("Bot started!")


for cmd in listdir("commands"):
    client.load_extension(f"commands.{cmd[:-3]}") if cmd.endswith(".py") else None

client.run(os.environ.get("BOT_TOKEN"))
