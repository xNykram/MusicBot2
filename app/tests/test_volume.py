import pytest
import discord.ext.test as dpytest
from unittest.mock import Mock
from discord.ext.commands import Context
from app.commands import volume as volume_module


@pytest.mark.asyncio
async def test_volume_wrong_range():
    await dpytest.message("!volume 0")
    assert (
        dpytest.verify().message().content("The volume number must be between 1 - 100")
    )


@pytest.mark.asyncio
async def test_volume_not_playing_songs(bot):
    dpytest.configure(client=bot, guilds=1, voice_channels=1)
    voice_client = Mock()
    voice_client.is_playing.return_value = True

    # Mock the guild voice_client method to return the mock voice_client
    pytest.MonkeyPatch.setattr(
        volume_module.volume.voice_client, "voice_client", voice_client
    )
    await dpytest.message("!volume 5")
    assert (
        dpytest.verify().message().content("The volume number must be between 1 - 100")
    )
