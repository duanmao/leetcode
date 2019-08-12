# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxdm = 0
        
        def getLevel(node):
            if (not node): return 0
            left = getLevel(node.left)
            right = getLevel(node.right)
            self.maxdm = max(self.maxdm, left + right)
            return max(left, right) + 1
    
        getLevel(root)
        return self.maxdm
