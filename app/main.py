import os
import logging
import asyncio
from sys import stdout
import discord
from discord.ext import commands
from api.client import Client


logging.basicConfig(stream=stdout, level=logging.INFO)
logger = logging.getLogger("main")


if os.environ.get("BOT_TOKEN") is None:
    raise ValueError("BOT_TOKEN environment variable not set")
BOT_TOKEN = os.environ.get("BOT_TOKEN") or ""

BOT_PREFIX = os.environ.get("PREFIX") or "!"
INTENTS = discord.Intents.default()
INTENTS.message_content = True


client = Client(
    command_prefix=commands.when_mentioned_or(BOT_PREFIX),
    case_insensitive=True,
    intents=INTENTS,
)


@client.event
async def on_ready():
    logging.info("Loaded prefix: %s", BOT_PREFIX)
    logging.info("Bot started!")
    for command in client.commands:
        logging.info("Loaded command: %s", command.name)


async def main():
    async with client:
        await client.start(BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
