import glob
import os

import discord.ext.test as dpytest
import pytest_asyncio
from discord import Intents
from discord.ext.commands import Bot

intents = Intents.all()


@pytest_asyncio.fixture
async def bot(event_loop) -> Bot:
    bot = Bot(intents=intents, command_prefix="!", loop=event_loop, help_command=None)
    for filename in os.listdir("app/commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"app.commands.{filename[:-3]}")
    await bot._async_setup_hook()
    dpytest.configure(bot)
    return bot


def pytest_sessionfinish() -> None:
    files = glob.glob("./dpytest_*.dat")
    for path in files:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error while deleting file {path}: {e}")
    print("\npySession closed successfully")
