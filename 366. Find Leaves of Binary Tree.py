# O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(node):
            if (not node): return 0
            level = max(dfs(node.left), dfs(node.right)) + 1
            if (len(res) < level): res.append([])
            res[level - 1].append(node.val) # note it should be level - 1 instead of level here
            return level

        dfs(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        leaves = { None }
        
        def getLeaves(node, level):
            if (not node or node in leaves): return # must check node in leaves
            if (node.left in leaves and node.right in leaves):
                level.append(node.val)
                leaves.add(node)
            else:
                getLeaves(node.left, level)
                getLeaves(node.right, level)
        
        if (not root): return [] # must have
        res = []
        while True:
            level = []
            getLeaves(root, level)
            res.append(level)
            if (root in leaves): break
        return res
