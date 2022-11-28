import os
import logging
import asyncio
import discord
from sys import stdout
from os import listdir
from discord.ext import commands

logging.basicConfig(stream=stdout, level=logging.INFO)
logger = logging.getLogger("main")


if os.environ.get('BOT_TOKEN') is None:
    raise ValueError("BOT_TOKEN environment variable not set")
else:
    BOT_TOKEN = os.environ.get('BOT_TOKEN') or ""

BOT_PREFIX = os.environ.get('PREFIX') or "!"
INTENTS = discord.Intents.default()
INTENTS.message_content = True

class Client(commands.Bot):
    queue_map: dict[int, list] = {}
    state_map: dict[int, "PLAYING"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue_map = {}

    async def setup_hook(self):
        for cmd in listdir('app/commands'):
            if cmd.endswith('.py') and cmd != '__init__.py':
                await self.load_extension(f'app.commands.{cmd[:-3]}')
                logger.info(f'Loaded {cmd[:-3]} command.')

    def get_queue(self, guild_id: int) -> list:
        if guild_id not in self.queue_map:
            self.queue_map[guild_id] = []

        return self.queue_map.get(guild_id, [])

client = Client(
    command_prefix=commands.when_mentioned_or(BOT_PREFIX),
    case_insensitive=True,
    intents=INTENTS
)


@client.event
async def on_ready():
    logging.info(f'Loaded prefix: {BOT_PREFIX}')
    logging.info("Bot started!")
    for command in client.commands:
        logging.info(f'Loaded command: {command}')

async def main():
    async with client:
        await client.start(BOT_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
