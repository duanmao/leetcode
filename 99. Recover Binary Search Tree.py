# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# True O(n)-time and O(1)-space solution
# https://leetcode.com/problems/recover-binary-search-tree/solution/ Approach 4 Morris

# Time: O(n), space: O(H)
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        s = []
        prev, node = None, root
        sus1 = sus2 = None
        while node or s:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            if prev and prev.val >= node.val:
                sus2 = node
                if not sus1: sus1 = prev
                else: break # There are only two swapped nodes here, and hence one could break after having the second node identified
            prev = node
            node = node.right

        sus1.val, sus2.val = sus2.val, sus1.val

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.sus1 = self.sus2 = None
        self.prev = None
        
        def traverse(node): # inorder
            if not node: return None
            traverse(node.left)
            if self.prev and self.prev.val >= node.val: # found suspects
                self.sus2 = node
                if not self.sus1: self.sus1 = self.prev 
                else: return # same as above, if self.sus1 is already assigned, we can directly return here
            self.prev = node
            traverse(node.right)
        
        traverse(root)
        self.sus1.val, self.sus2.val = self.sus2.val, self.sus1.val

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.sus1 = self.sus2 = None
        
        def traverse(prev, node): # inorder
            if not node: return None
            left = traverse(prev, node.left)
            if left: prev = left
            if prev and prev.val >= node.val: # found suspects
                if not self.sus1: self.sus1 = prev
                self.sus2 = node
            right = traverse(node, node.right)
            return right if right else node
        
        traverse(None, root)
        self.sus1.val, self.sus2.val = self.sus2.val, self.sus1.val
