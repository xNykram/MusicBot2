from typing import Any
from pydantic import BaseModel


class Song(BaseModel):
    id: str
    name: str
    url: str
    duration: str
    requester: Any

    def display(self):
        return "{} ({})".format(self.title, self.duration)
