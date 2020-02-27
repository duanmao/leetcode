# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        dq = collections.deque([root])
        res = []
        left2right = True
        while dq:
            n = len(dq)
            level = [0] * n
            for i in range(n):
                node = dq.popleft()
                if left2right: level[i] = node.val
                else: level[n - i - 1] = node.val
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            res.append(level)
            left2right = not left2right
        return res
