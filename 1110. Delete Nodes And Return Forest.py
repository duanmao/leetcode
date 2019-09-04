# Time: O(n), space: O(1) if the recursion stack and the result array don't count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        
        # return root of this subtree, i.e., node itself if not deleted, otherwise None
        def dfs(node, is_root):
            if (not node): return None
            deleted = node.val in to_delete
            if (is_root and not deleted):
                res.append(node)
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            return node if not deleted else None
            
        dfs(root, True)
        return res

# not very beautifully... though works
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        
        def dfs(node, parent):
            if (not node): return
            dfs(node.left, node)
            dfs(node.right, node)
            if (node.val in to_delete):
                if (node.left): res.append(node.left)
                if (node.right): res.append(node.right)
                if (parent and node == parent.left): parent.left = None
                elif (parent): parent.right = None
                
        if (root.val not in to_delete): res.append(root) # must have
        dfs(root, None)
        return res
