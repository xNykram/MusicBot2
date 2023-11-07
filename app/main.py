import asyncio
import logging
import os
from sys import stdout

import discord
from discord.ext import commands

from app.core.settings import config

# logging.basicConfig(filename='/app/logs/log.txt', level=logging.INFO)
logger = logging.getLogger("main")

if os.environ.get("BOT_TOKEN") is None:
    raise ValueError("BOT_TOKEN environment variable not set")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix=config.BOT_PREFIX, intents=intents)

@client.event
async def on_ready():
    for filename in os.listdir('app/commands'):
        if filename.endswith('.py'):
            await client.load_extension(f"app.commands.{filename[:-3]}")



@client.event
async def on_voice_state_update(member, before, after):
    voice_client = client.voice_clients[0] if client.voice_clients else None
    if voice_client:
        if len(voice_client.channel.members) == 1:
            await voice_client.disconnect()


def main():
         client.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
