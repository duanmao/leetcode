"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node: return None
        if node.right:
            nd = node.right
            while nd.left:
                nd = nd.left
            return nd
        else:
            nd = node
            while nd.parent:
                if nd == nd.parent.left: return nd.parent
                nd = nd.parent
            return None
