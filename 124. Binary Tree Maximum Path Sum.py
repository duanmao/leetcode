# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def pathSum(node):
            if (not node):
                return 0
            left = max(pathSum(node.left), 0)
            right = max(pathSum(node.right), 0)            
            self.maxSum = max(self.maxSum, left + node.val + right)
            return max(left, right) + node.val
        
        self.maxSum = float('-inf')
        pathSum(root)
        return self.maxSum
