# Time: O(V + E), space: O(V + E)
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me
# the core is to remove cycles within a graph
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        for v1, v2 in connections:
            graph[v1].append(v2)
            graph[v2].append(v1)
        ranks = [-1] * n # initial rank for each vertex, -1 denotes unvisited
        criticals = []
        
        def dfs(pre, v, rk):
            if ranks[v] >= 0: return ranks[v] # current vertex has been visited before
            ranks[v] = rk
            for nb in graph[v]:
                if nb == pre: continue # skip the current vertex's parent (where it comes from)
                nextrk = dfs(v, nb, rk + 1)
                ranks[v] = min(ranks[v], nextrk)
                if nextrk >= rk + 1: # not further cycle found for this neighbor
                    criticals.append([v, nb])
            return ranks[v]
        
        dfs(-1, 0, 0)
        return criticals
