# dictionary + double linked list
# both operations take O(1)
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
