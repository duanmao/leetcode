# Time: O((log h)^2), space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(root):
            if (not root): return 0
            return height(root.left) + 1

        if (not root): return 0
        lefth, righth = height(root.left), height(root.right)
        if (lefth == righth):
            return pow(2, lefth) + self.countNodes(root.right)
        else:
            return pow(2, righth) + self.countNodes(root.left)

# Time: O(n), space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if (not root): return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
