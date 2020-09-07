from collections import deque
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.queue = deque()

    # @return an integer
    def get(self, key):
        if key in self.cache :
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        while len(self.queue) >= self.capacity :
            k = self.queue.popleft()
            del(self.cache[k])
        self.cache[key] = value
        self.queue.append(key)
        
        
