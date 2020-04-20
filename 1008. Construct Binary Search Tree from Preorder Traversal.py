# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)
# Space: O(n) worst case, O(h) average case for the stack, where h is the height of the tree.
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.cur = 0

        def build(high):
            if self.cur >= len(preorder) or preorder[self.cur] > high: return None
            root = TreeNode(preorder[self.cur])
            self.cur += 1
            root.left = build(root.val)
            root.right = build(high)
            return root

        return build(float('inf'))

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        nodes = [root]
        for num in preorder[1:]:
            node = TreeNode(num)
            if num < nodes[-1].val:
                nodes[-1].left = node
            else:
                while nodes and nodes[-1].val < num:
                    parent = nodes.pop()
                parent.right = node
            nodes.append(node)
        return root

# Time: O(nlogn)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(low, high):
            if low >= high: return None
            root = TreeNode(preorder[low])
            sep = bisect.bisect(preorder, preorder[low], low, high)
            root.left = build(low + 1, sep)
            root.right = build(sep, high)
            return root
        
        return build(0, len(preorder))

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(low, high):
            if low > high: return None
            root = TreeNode(preorder[low])
            l, h = low + 1, high
            while l <= h:
                mid = (l + h) // 2
                if preorder[mid] < preorder[low]: l = mid + 1
                else: h = mid - 1
            root.left = build(low + 1, l - 1)
            root.right = build(l, high)
            return root

        return build(0, len(preorder) - 1)

# Time: O(n^2), since slicing the array takes time too
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        low, high = 1, len(preorder) - 1
        while low <= high:
            mid = (low + high) // 2
            if preorder[mid] < preorder[0]: low = mid + 1
            else: high = mid - 1
        root.left = self.bstFromPreorder(preorder[1:low])
        root.right = self.bstFromPreorder(preorder[low:])
        return root
