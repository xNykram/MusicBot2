from pydantic import BaseModel

from .song import Song


class Queue(BaseModel):
    queue: list = []

    def enqueue(self, item: Song):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return
        return self.queue.pop(0)

    def clear(self):
        self.queue = []

    def size(self):
        return len(self.queue)
