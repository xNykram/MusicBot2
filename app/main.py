import os
import logging
import asyncio
from sys import stdout
import discord
from discord.ext import commands
from app.core.client import Client

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


@client.event
async def on_voice_state_update(member, before, after):
    voice_client = client.voice_clients[0] if client.voice_clients else None
    if voice_client:
        if len(voice_client.channel.members) == 1:
            await voice_client.disconnect()


async def main():
    async with client:
        await client.start(BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
