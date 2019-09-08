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
        def findNext(node):
            while (node):
                if (node.left): return node.left
                if (node.right): return node.right
                node = node.next
            return None
                
        if (not root): return root
        if (not root.left and not root.right): return root
        if (root.left):
            if (root.right): root.left.next = root.right
            else: root.left.next = findNext(root.next)
        if (root.right):
            root.right.next = findNext(root.next)
        # must handle RIGHT child first
        # consider this tree below
        #              1
        #       2             9
        #    3     5	  10     11
        # 4      6   7         12  13
        #           8
        self.connect(root.right) 
        self.connect(root.left)
        return root
