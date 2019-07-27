# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        s = []
        prev = None
        while (root or len(s)):
            while (root):
                s.append(root)
                root = root.left
            root = s.pop()
            if (prev and root.val <= prev.val):
                return False
            prev = root
            root = root.right
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(log(n)), space: O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node, low, high):
            if (not node):
                return True
            if (low < node.val < high):
                return check(node.left, low, node.val) and check(node.right, node.val, high)
            else:
                return False
            
        return check(root, float('-inf'), float('inf'))
