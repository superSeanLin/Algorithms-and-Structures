class LRUCache:

    def __init__(self, capacity: 'int'):
        self.cache = {}
        self.capacity = capacity
        self.queue = []

    def get(self, key: 'int') -> 'int':
        if key in self.cache and self.cache[key] != -1:
            self.queue = self.updateQ(self.queue, key)  # valid update
            return self.cache[key]
        else:
            return -1

    def put(self, key: 'int', value: 'int') -> 'None':
        if not key in self.queue and len(self.queue)+1 > self.capacity:  # need eviction
            evict = self.queue.pop(0)
            self.cache[evict] = -1
        self.queue = self.updateQ(self.queue, key)  # make sure queue is the right length and concise
        self.cache[key] = value
    
    def updateQ(self, queue, key):  # same key should be updated
        queue = [e for e in queue if e != key]
        queue.append(key)
        while len(queue) > self.capacity:
            queue.pop(0)
        return queue

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
