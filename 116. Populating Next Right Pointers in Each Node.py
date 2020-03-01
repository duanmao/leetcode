"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.right)
        self.connect(root.left)
        return root

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
