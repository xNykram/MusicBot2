import pytest
import discord.ext.test as dpytest
from app.core.player import mp


@pytest.mark.asyncio
async def test_clear_songs(bot, monkeypatch):
    
    async def mock_return_queue(guild_id):
        return ["fake_song"]
    monkeypatch.setattr(mp, 'return_queue', mock_return_queue)
    await dpytest.message("!clear")
    
    assert dpytest.verify().message().content("The queue has been cleared.")
    assert len(mp.queue) == 0


@pytest.mark.asyncio
async def test_clear_no_songs(bot):
    await dpytest.message("!clear")
    
    assert dpytest.verify().message().content("There is nothing to clear.")
