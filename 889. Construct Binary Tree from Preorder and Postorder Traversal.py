# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)
# Time: O(n), space: O(height)
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        self.preidx = self.postidx = 0

        def construct():
            root = TreeNode(pre[self.preidx])
            self.preidx += 1
            if (root.val != post[self.postidx]):
                root.left = construct()
            if (root.val != post[self.postidx]):
                root.right = construct()
            self.postidx += 1
            return root

        return construct()

# Time: O(n^2) for we use n time to find the index so as to split the array for left and right
# subtree in each recursion
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def construct(prelow, prehigh, postlow, posthigh):
            if (prelow > prehigh): return None
            root = TreeNode(pre[prelow])
            if (prelow == prehigh): return root
            
            leftchild = pre[prelow + 1]
            idx = post.index(leftchild)
            leftcount = idx - postlow + 1
            root.left = construct(prelow + 1, prelow + leftcount, postlow, idx)
            root.right = construct(prelow + leftcount + 1, prehigh, idx + 1, posthigh - 1)
            return root
        
        return construct(0, len(pre) - 1, 0, len(post) - 1)
