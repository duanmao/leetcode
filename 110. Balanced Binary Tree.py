# Time: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balance = True
        
        def check(node):
            if (not node): return 0
            left, right = check(node.left), check(node.right)
            if (abs(left - right) > 1): self.balance = False
            return max(left, right) + 1
        
        check(root)
        return self.balance
