# Time: O(n), space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # cannot be done by binary search with time O(logN)
        # O(N) is what we can do best
        
        if (not head):
            node = Node(insertVal, None)
            node.next = node
            return node
        
        pre, node = None, head
        while (True):
            pre = node
            node = node.next
            if ((pre.val <= insertVal <= node.val) or # most regular case
                # pre.val > node.val means we're at the *true* beginning of the *sorted* list
                # we need to decide whether the new val belongs to here
                # i.e., whether it's smaller or larger than all existing values
                (pre.val > node.val and (insertVal <= node.val or insertVal >= pre.val)) or
                # all other positions have been checked and no suitable places found
                # the only place we have not checked is the one before head, so it must be the answer
                (node == head)):
                newnode = Node(insertVal, node)
                pre.next = newnode
                break
        return head
