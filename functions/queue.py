# Class Queue

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty():
        return len(self.items) == 0

    def size():
        return len(self.items)

