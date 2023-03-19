import os
import logging
import asyncio
from sys import stdout
import discord
from discord.ext import commands
from app.api.client import Client

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
    if before.channel is not None and after.channel is None:
        if len(before.channel.members) == 1:
            if before.channel.guild.voice_client.is_playing():
                return
            await before.channel.guild.voice_client.disconnect()


async def main():
    async with client:
        await client.start(BOT_TOKEN)


if __name__ == "__main__":
    if os.environ.get("APP_ENV") == "Dev":
        import debugpy

        debugpy.listen(("0.0.0.0", 5678))
    asyncio.run(main())
