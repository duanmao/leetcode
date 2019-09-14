# dfs
# Time: O(n), space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def dfs(node: TreeNode, k: int) -> (int,int,int):
            if not node:
                return float('Inf'), 0, 0
            if not node.left and not node.right:
                return 1, int(node.val == k), node.val
            else:
                lLeafDist, lTargetDist, lLeafVal = dfs(node.left, k)
                rLeafDist, rTargetDist, rLeafVal = dfs(node.right, k)

                if node.val == k:
                    if lLeafDist < rLeafDist:
                        return lLeafDist, 1, lLeafVal
                    else:
                        return rLeafDist, 1, rLeafVal
                elif lTargetDist: # found the target in the left subtree
                    # length of the path which sets out from the target,
                    # passing through the current node and ultimately ends in this node's *right* subtree
                    passMe = lTargetDist + rLeafDist
                    if lLeafDist < passMe:
                        return lLeafDist, lTargetDist + 1, lLeafVal
                    else:
                        return passMe, lTargetDist + 1, rLeafVal
                elif rTargetDist: # found the target in the right subtree
                    # length of the path which sets out from the target,
                    # passing through the current node and ultimately ends in this node's *left* subtree
                    passMe = rTargetDist + lLeafDist
                    if rLeafDist < passMe:
                        return rLeafDist, rTargetDist + 1, rLeafVal
                    else:
                        return passMe, rTargetDist + 1, lLeafVal
                else:
                    if lLeafDist < rLeafDist:
                        return lLeafDist + 1, 0, lLeafVal
                    else:
                        return rLeafDist + 1, 0, rLeafVal

        return dfs(root,k)[2]


# convert to undirected graph
# both O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        
        # must standing at the child and adding the edges between the child and its parent
        # cannot do the opposite of standing at a parent and adding the edges of its children
        # as the later graph length check for leaves won't work in the opposite way
        def dfs(node, parent = None):
            if (not node): return
            if (node.val == k): self.start = node
            graph[parent].append(node)
            graph[node].append(parent)
            dfs(node.left, node)
            dfs(node.right, node)
        
        def bfs():
            queue = collections.deque([self.start])
            added = {k}
            while (queue):
                cur = queue.popleft()
                if (cur):
                    if (len(graph[cur]) <= 1):
                        return cur.val
                    for nxt in graph[cur]:
                        if (nxt not in added):
                            queue.append(nxt)
                            added.add(nxt)
            return -1
                        
        dfs(root)
        return bfs()
