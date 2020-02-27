# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dm = 0
        
        def traverse(node):
            if not node: return 0
            left, right = traverse(node.left), traverse(node.right)
            self.dm = max(self.dm, left + right)
            return max(left, right) + 1
        
        traverse(root)
        return self.dm
