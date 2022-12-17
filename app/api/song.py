from discord import Member


class Song:
    def __init__(self, url: str, title: str, duration: int, requester: Member):
        self.url = url
        self.title = title
        self.duration = duration
        self.requester = requester

    def __str__(self):
        return f"{self.title} ({self.duration})"
