# Time: O(min(n1, n2)), space: O(min(h1, h2)). n: # of node, h: height of tree
# because "Each value in each tree will be a unique integer in the range"
# if there're duplicate values in the tree, the time complexity will be O(n^2) because now we may
# check down to the bottom for all the subtrees, there're 4 calls of it, so 
# T(N) = 4T(N/2) + O(1) = 4 ^ (log N) + O(1) => T(N) = O(N^2)
# However, because the values are unique, we won't traverse all nodes in all four calls. Half of 
# the recursive calls will immediately return, so the coefficient of 4 in the equation above will
# shrink to 2, i.e. "4 T(N/2)" can be upgraded to 2 T(N/2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if (not root1 and not root2): return True
        elif (not root1 or not root2): return False
        elif (root1.val != root2.val): return False # Don't forget this!!!
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
            (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root2.left, root1.right))
