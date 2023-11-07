import glob
import os
import pytest
import discord
import discord.ext.commands as commands
import discord.ext.test as test

import app as discord_bot


@pytest.fixture
def client(event_loop):
    c = discord.Client(loop=event_loop)
    test.configure(c)
    return c


@pytest.fixture
def bot(request, event_loop):
    intents = discord.Intents.default()
    intents.members = True
    b = commands.Bot("!", loop=event_loop, intents=intents)

    marks = request.function.pytestmark
    mark = None
    for mark in marks:
        if mark.name == "command":
            break

    if mark is not None:
        for extension in mark.args:
            b.load_extension(f".commands.{extension}", package="discord_bot")
            # b.load_extension(f"discord_bot.commands.{extension}")

    test.configure(b)
    return b


@pytest.fixture(autouse=True)
async def cleanup():
    yield
    await test.empty_queue()


def pytest_sessionfinish(session, exitstatus):
    """Code to execute after all tests."""

    # dat files are created when using attachements
    print("\n-------------------------\nClean dpytest_*.dat files")
    fileList = glob.glob("./dpytest_*.dat")
    for filePath in fileList:
        try:
            os.remove(filePath)
        except Exception:
            print("Error while deleting file : ", filePath)
