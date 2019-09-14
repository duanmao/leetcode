# https://leetcode.com/problems/binary-tree-coloring-game/discuss/350570/JavaC%2B%2BPython-Simple-recursion-and-Follow-Up
# Time: O(n), space: O(height)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def countNodes(node):
            if (not node): return 0
            left = countNodes(node.left)
            right = countNodes(node.right)
            if (node.val == x):
                self.left = left
                self.right = right
            return left + right + 1
        
        countNodes(root)
        self.parent = n - self.left - self.right - 1
        mybest = max(self.left, self.right, self.parent)
        return mybest > n // 2
