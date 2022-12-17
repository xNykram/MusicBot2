from typing import Any
from pydantic import BaseModel


class Connections(BaseModel):
    id: int
    guild_id: int
    channel_id: int
    voice_client: Any
