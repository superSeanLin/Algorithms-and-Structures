class DoubleLinkedNode:
    def __init__(self, key, value):
        self.pre = None
        self.nxt = None
        self.val = value
        self.key = key 
    
class LRUCache:
    # use hashmap with double linked list to achieve O(1); the important property of double linked list is that we can delete a node without knowing other node
    # Note: also we can not delete node from cache, instead, we set value to -1
    def __init__(self, capacity: int):
        self.cache = {}  # key : node
        self.count = 0
        self.capacity = capacity
        self.head, self.tail = DoubleLinkedNode(-1, -1), DoubleLinkedNode(-1, -1)  # set boundery
        self.head.nxt = self.tail
        self.tail.pre = self.head
    
    def remove(self, node):
        pre = node.pre
        nxt = node.nxt
        pre.nxt = nxt
        nxt.pre = pre
    
    def addToHead(self, node):
        temp = self.head.nxt
        self.head.nxt = node
        node.pre = self.head
        node.nxt = temp
        temp.pre = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.addToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # update
            node = self.cache[key]
            self.remove(node)
            self.addToHead(node)
            node.val = value
        else:
            node = DoubleLinkedNode(key, value)
            self.addToHead(node)
            self.count += 1
            if self.count > self.capacity:
                temp = self.tail.pre
                self.remove(temp)
                del self.cache[temp.key]  # delete node in hashmap is O(1)
                self.count -= 1
            self.cache[key] = node
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
