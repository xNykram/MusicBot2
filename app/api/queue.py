from song import Song


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: Song):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
