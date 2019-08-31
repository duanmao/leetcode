# O(nlogn) time and O(n) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        
        def dfs(node, x, y):
            if (not node): return
            nodes.append((x, y, node.val))
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)
            
        dfs(root, 0, 0)
        nodes.sort()
        prevx = float('-inf')
        res, cur = [], []
        for x, y, val in nodes:
            if (x != prevx):
                res.append([])
                prevx = x
            res[-1].append(val)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        level = [(root, 0)] # (node, x)
        verts = collections.defaultdict(list)
        while level:
            thislevel = collections.defaultdict(list)
            nextlevel = []
            for node, x in level:
                if (node.left): nextlevel.append((node.left, x - 1))
                if (node.right): nextlevel.append((node.right, x + 1))
                thislevel[x].append(node.val)
            for x in thislevel:
                verts[x].extend(sorted(thislevel[x]))
            level = nextlevel
        
        return [verts[x] for x in sorted(verts)]

# very slow
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        poses = collections.defaultdict(list)
        self.minx = self.maxx = self.maxy = 0
        
        def getCoors(node, x, y):
            if (not node): return
            self.minx = min(self.minx, x)
            self.maxx = max(self.maxx, x)
            self.maxy = max(self.maxy, y)
            poses[(x, y)].append(node.val)
            getCoors(node.left, x - 1, y + 1)
            getCoors(node.right, x + 1, y + 1)
            
        getCoors(root, 0, 0)
        res = []
        for i in range(self.minx, self.maxx + 1):
            level = []
            for j in range(self.maxy + 1):
                if ((i, j) in poses):
                    level.extend(sorted(poses[(i, j)]))
            res.append(level)
        
        return res
