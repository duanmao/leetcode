# dictionary + double linked list
# both operations take O(1)
class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, self.head, None)
        self.head.next = self.tail
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.__remove(key)
            self.__add(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.__remove(key)
        self.__add(key, value)

    def __add(self, key, val):
        if len(self.cache) >= self.limit:
            self.__remove(self.tail.prev.key)
        node = Node(key, val, self.head, self.head.next)
        self.cache[key] = self.head.next = node.next.prev = node #

    def __remove(self, key):
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.cache[key]

class Node:
    def __init__(self, key, val, prev, nxt):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



class Node:
    def __init__(self, key, val, prev, nxt):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if (key not in self.dic):
            return -1
        node = self.dic[key]
        self.__remove(node)
        self.put(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if (key in self.dic): # remember to check if already exists
            self.__remove(self.dic[key]) # if exists, must remove it first
        if (len(self.dic) >= self.capacity):
            self.__remove(self.head)
        self.__add(key, value)

    def __remove(self, node):
        if (node == self.head): self.head = node.next
        if (node == self.tail): self.tail = node.prev
        if (node.prev): node.prev.next = node.next
        if (node.next): node.next.prev = node.prev
        del self.dic[node.key]

    def __add(self, key, val):
        node = Node(key, val, self.tail, None)
        self.dic[key] = node
        if (self.tail): self.tail.next = node
        self.tail = node
        if (not self.head): self.head = node # remember to assign head

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
