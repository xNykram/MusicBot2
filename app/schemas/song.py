from pydantic import BaseModel


class Song(BaseModel):
    id: int
    name: str
    url: str
    duration: str
