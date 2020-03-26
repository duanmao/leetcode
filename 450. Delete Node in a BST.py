# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/delete-node-in-a-bst/solution/
# Time: O(H) = O(logn) (balanced tree), space: O(H), where H is the height of the tree
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def predecessor(node):
            if not node or not node.left: return None
            node = node.left
            while node.right: node = node.right
            return node
        
        def successor(node):
            if not node or not node.right: return None
            node = node.right
            while node.left: node = node.left
            return node
        
        if not root: return None
        if root.val == key:
            if not root.left and not root.right:
                root = None
            elif root.right:
                suc = successor(root)
                root.val = suc.val
                root.right = self.deleteNode(root.right, root.val) # must assign root.right
            else:
                pre = predecessor(root)
                root.val = pre.val
                root.left = self.deleteNode(root.left, root.val) # must assign root.left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key) # must assign root.right
        else:
            root.left = self.deleteNode(root.left, key) # must assign root.left
            
        return root
