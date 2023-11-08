import glob
import os
import discord.ext.commands as commands
import discord.ext.test as dpytest
import pytest_asyncio
from discord.ext.commands import Bot
from discord import Intents
import logging

intents = Intents.all()

@pytest_asyncio.fixture
async def bot(event_loop):
    bot = Bot(intents=intents, command_prefix="!", loop=event_loop, help_command=None)
    for filename in os.listdir("/app/app/commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"app.commands.{filename[:-3]}")
    await bot._async_setup_hook()
    dpytest.configure(bot)
    return bot

def pytest_sessionfinish():
    files = glob.glob("./dpytest_*.dat")
    for path in files:
        try:
            os.remove(path)
        except Exception as e:
            print(f"Error while deleting file {path}: {e}")
    print("\npySession closed successfully")
