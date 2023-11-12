import logging
import os

import discord
from discord.ext import commands

from app.core.settings import config

logger = logging.getLogger("main")

if os.environ.get("BOT_TOKEN") is None:
    raise ValueError("BOT_TOKEN environment variable not set")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix=config.BOT_PREFIX, intents=intents, help_command=None)


@client.event
async def on_ready() -> None:
    for filename in os.listdir("app/commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"app.commands.{filename[:-3]}")
    logger.warning(msg="All commands loaded!")


@client.event
async def on_voice_state_update(member, before, after) -> None:
    voice_client = client.voice_clients[0] if client.voice_clients else None
    if voice_client:
        if len(voice_client.channel.members) == 1:
            await voice_client.disconnect()


@client.event
async def on_command_error(ctx, error) -> None:
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command does not exist.")
    else:
        logging.warning(error)


def main() -> None:
    client.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
