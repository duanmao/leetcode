# Time: O(n), space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # in order to fast retrieve random node during copy,
        # we must have a direct link from the old list nodes to the new ones
        # thus, we first point each old node to its copy using the next pointer
        # and use the new nodes' next to link the olds' next (1st traversal),
        # so that we can quickly trace the copied new nodes
        # to which the random pointers attach to
        # simply by accessing the old nodes' randoms' next, which makes the 2nd go
        # and we need a final third loop to recover the old list
        # as well as also set the next pointers of the new nodes right
        if not head: return None
        node = head
        while node:
            node.next = Node(node.val, node.next, None)
            node = node.next.next
        cphead = head.next
        node = head
        while node:
            if node.random: node.next.random = node.random.next # must do safety check
            node = node.next.next
        node = head
        while node:
            cp = node.next
            node.next = node.next.next
            if node.next: cp.next = node.next.next # must do safety check
            node = node.next
        return cphead

# same one, verbose implementation
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

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        nodesmap = {}
        node = head
        while node: 
            nodesmap[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            if node.next: nodesmap[node].next = nodesmap[node.next]
            if node.random: nodesmap[node].random = nodesmap[node.random]
            node = node.next
        return nodesmap[head]
