import pytest
import discord.ext.test as dpytest

@pytest.mark.asyncio
async def test_help_command(bot):
    await dpytest.message("!help")

    assert dpytest.verify().message()