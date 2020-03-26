# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            node = root
            s = []
            nums = []
            while node or s:
                while node:
                    s.append(node)
                    node = node.left
                node = s.pop()
                nums.append(node.val)
                node = node.right
            return nums
        
        def build(nums, low, high):
            if low > high: return None
            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = build(nums, low, mid - 1)
            root.right = build(nums, mid + 1, high)
            return root
        
        nums = inorder(root)
        return build(nums, 0, len(nums) - 1)
