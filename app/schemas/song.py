from typing import Any
from pydantic import BaseModel


class Song(BaseModel):
    id: str
    name: str
    url: str
    duration: str
    requester: Any
