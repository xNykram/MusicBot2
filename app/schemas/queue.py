from pydantic import BaseModel

from .song import Song


class Queue(BaseModel):
    queue: list = []

    def enqueue(self, item: Song):
        self.queue.append(item)

    def clear(self):
        self.queue = []

    def size(self):
        return len(self.queue)
