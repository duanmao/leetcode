# Time: O(n), space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if (not head):
            return None
        node = head
        while (node):
            nnext = node.next
            cpnode = Node(node.val, node.next, None)
            node.next = cpnode
            node = nnext
        node = head
        cphead = head.next
        while (node):
            node.next.random = node.random.next if node.random else None
            node = node.next.next
        node = head
        while (node):
            nnext = node.next.next
            node.next.next = nnext.next if nnext else None
            node.next = nnext
            node = nnext
        
        return cphead

# Time: O(n), space: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if (not head):
            return None
        # cphead = Node(0, None, None)
        d = {None: None}
        node = head
        while (node):
            d[node] = Node(node.val, node.next, node.random)
            node = node.next
        cphead = d[head]
        node = head
        while (node):
            d[node].next = d[node.next]
            d[node].random = d[node.random]
            node = node.next
        return cphead
