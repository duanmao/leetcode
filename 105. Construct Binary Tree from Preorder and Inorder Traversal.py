# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n), space: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        vtoi = dict((v, i) for i, v in enumerate(inorder))

        def build(preorder, plow, phigh, inorder, ilow, ihigh):
            if plow > phigh: return None
            root = TreeNode(preorder[plow])
            i = vtoi[preorder[plow]]
            root.left = build(preorder, plow + 1, plow + i - ilow, inorder, ilow, i - 1)
            root.right = build(preorder, plow + i - ilow + 1, phigh, inorder, i + 1, ihigh)
            return root

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

# short and clear, but costs more time and space
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root
