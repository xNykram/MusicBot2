from os import listdir

from discord.ext import commands


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue_map = {}
        self.connections = []

    async def setup_hook(self):
        for cmd in listdir("/app/app/commands"):
            if cmd.endswith(".py") and cmd != "__init__.py":
                await self.load_extension(f"app.commands.{cmd[:-3]}")

    def get_queue(self, guild_id: str) -> list:
        if guild_id not in self.queue_map:
            self.queue_map[guild_id] = []

        return self.queue_map.get(guild_id, [])
