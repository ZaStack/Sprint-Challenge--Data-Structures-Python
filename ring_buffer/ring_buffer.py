class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        self.storage[self.index] = item
        self.index += 1
        if self.index > (self.capacity - 1):
            self.index = 0

    def get(self):
        return self.storage

