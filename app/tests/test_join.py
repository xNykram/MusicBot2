import pytest
import discord.ext.test as dpytest
from discord.ext.commands import Bot
from app.commands import join
from discord import VoiceChannel

@pytest.mark.asyncio
async def test_join_command_user_not_in_channel(bot):
    await dpytest.message("!join")

    assert dpytest.verify().message().content("You are not connected to a voice channel.")

@pytest.mark.asyncio
async def test_join_command_connected(bot: Bot, mocker):
    author_voice_channel = bot.get_all_channels()
    voice_channel = [channel for channel in author_voice_channel if channel.name == "VoiceChannel_0"]
    print(voice_channel)
    mocker.patch('app.commands.join.get_channel', return_value=voice_channel[0])
    await dpytest.message("!join")
    assert dpytest.verify().message().content("You are not co;nnected to a voice channel.")
    
    