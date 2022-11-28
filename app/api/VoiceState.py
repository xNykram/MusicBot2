from discord.ext.commands.context import Context
from .Queue import Queue

class VoiceState:
    """
    This is a class that is used to store the bot state for a guild (discord server).
    """
    def __init__(self, ctx: Context):
        if ctx.guild is None:
            raise AttributeError('Context has no guild attribute.')
        self.guild_id = ctx.guild.id
        self.queue: Queue = Queue()
