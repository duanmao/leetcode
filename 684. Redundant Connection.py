# a simple connected graph with no cycle is a tree

# Union-Find
# We simply find the first edge occurring in the graph that is already connected.
# O(n)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        
        def find(x):
            if (x not in parent): parent[x] = x
            if (parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parentx = find(x)
            parenty = find(y)
            if (parentx == parenty): return True
            parent[parentx] = parenty
            return False
        
        for edge in edges:
            x, y = edge
            if (union(x, y)): return edge
        return None

# For each edge (u, v), traverse the graph with a depth-first search to see if we can already
# connect u and v with the previous edges. If we can, then it must be the duplicate edge.
# DFS
# Time: O(n^2), space: O(n)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        visited = set()
        
        def dfs(start, end):
            if (start == end): return True
            visited.add(start)
            for nxt in graph[start]:
                if (nxt not in visited and dfs(nxt, end)):
                    return True
            visited.remove(start)
            return False
        
        for edge in edges:
            s, e = edge
            if (s in graph and e in graph and dfs(s, e)): return edge
            graph[s].append(e)
            graph[e].append(s)
        return None
