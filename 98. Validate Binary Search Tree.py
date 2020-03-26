# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        s = []
        prev, node = None, root
        while node or s:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            if prev and prev.val >= node.val: return False
            prev = node
            node = node.right
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n), space: O(1)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValid(node, vmin, vmax):
            if not node: return True
            if not vmin < node.val < vmax: return False
            return isValid(node.left, vmin, node.val) and isValid(node.right, node.val, vmax)

        return isValid(root, float('-inf'), float('inf'))
