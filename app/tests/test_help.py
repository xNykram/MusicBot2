import discord.ext.test as dpytest
import pytest
from discord.ext.commands import Bot


@pytest.mark.asyncio
async def test_help_command(bot: Bot) -> None:
    await dpytest.message("!help")

    assert dpytest.verify().message()
