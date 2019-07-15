"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def conn(parent, node):
            if (not node):
                return
            if (parent):
                if (node == parent.left):
                    node.next = parent.right
                else:
                    if (parent.next):
                        node.next = parent.next.left
            conn(node, node.left)
            conn(node, node.right)
            
        conn(None, root)
        return root
