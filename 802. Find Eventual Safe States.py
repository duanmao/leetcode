# topological sort of reversed graph (edges are reversed)
# Time: O(V + E) if omit the last sorting step, space: O(V)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rgraph = collections.defaultdict(list)
        n = len(graph)
        indegree = [0] * n
        res = []
        for i in range(n):
            indegree[i] = len(graph[i])
            if (not indegree[i]): res.append(i)
            for j in graph[i]:
                rgraph[j].append(i)

        for safe in res:
            for nxt in rgraph[safe]:
                indegree[nxt] -= 1
                if (indegree[nxt] == 0):
                    res.append(nxt)
        return sorted(res)

# longer version of exactly the same thing as above
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rgraph = collections.defaultdict(list)
        n = len(graph)
        indegree = [0] * n
        for i in range(n):
            for j in graph[i]:
                rgraph[j].append(i)
                indegree[i] += 1
                
        termis = []
        for i in range(n):
            if (indegree[i] == 0): termis.append(i)
                
        res = []
        while (termis):
            cur = termis.pop()
            res.append(cur)
            for nxt in rgraph[cur]:
                indegree[nxt] -= 1
                if (indegree[nxt] == 0):
                    termis.append(nxt)
        return sorted(res)

# dfs
# Time: O(V + E), space: O(V)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        # 0 for unvisited, 1 for visiting, 2 for visited
        visited = [0] * n

        def dfs(vi):
            if (visited[vi] == 1): # found a circle
                return True
            elif (visited[vi] == 0):
                visited[vi] = 1
                for i in graph[vi]:
                    if (dfs(i)): return True
                visited[vi] = 2
                res.append(vi)
                return False

        for i in range(n):
            if (visited[i] == 0):
                dfs(i)
        return sorted(res)
