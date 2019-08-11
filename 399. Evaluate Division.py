# Union Find
# O(n) since union find operation is pretty much constant, I guess
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a/b = v1 -> parent[a] = b, ratio[a] = v1
        # b/c = v2 -> parent[b] = c, ratio[b] = v2
        parent = {}
        ratio = {}

        def find(x):
            if (x not in parent):
                parent[x], ratio[x] = x, 1
            if (not parent[x] == x):
                r = find(parent[x])
                # path compression
                # x/parent = ratio[x], parent/root = ratio[parent]
                # => x/root = x/parent * parent/r
                ratio[x] *= ratio[parent[x]]
                parent[x] = r
            return parent[x]

        def union(x1, x2, val):
            p1, p2 = find(x1), find(x2)
            parent[p1] = p2
            # x1/p1 = ratio[x1], x1/x2 = val, x2/p2 = ratio[x2]   =>
            # p1/p2 = x2/p2 * x1/x2 / x1/p1
            ratio[p1] = val * ratio[x2] / ratio[x1]

        for [e1, e2], v in zip(equations, values):
            union(e1, e2, v)

        res = []
        for q1, q2 in queries:
            if (q1 not in parent or q2 not in parent or not find(q1) == find(q2)):
                res.append(-1)
            else:
                # q1/r = ratio[q1], q2/r = ratio[q2] => q1/q2
                res.append(ratio[q1] / ratio[q2])
        return res

# Graph
# O(V+E)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for [e1, e2], v in zip(equations, values):
            graph[e1].append((e2, v))
            graph[e2].append((e1, 1/v))

        def dfs(src, trg, cur, visited):
            if (src == trg):
                return cur
            else:
                visited.add(src)
                for nb, v in graph[src]:
                    if (nb not in visited):
                        mul = dfs(nb, trg, cur * v, visited)
                        if (not mul == -1):
                            return mul
                visited.remove(src)
                return -1

        varis = set(graph.keys())
        res = []
        for q1, q2 in queries:
            if (not q1 in varis or not q2 in varis):
                res.append(-1)
            else:
                visited = set()
                res.append(dfs(q1, q2, 1, visited))
        return res

# Floyd–Warshall
# O(n^3)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:    
        eqs = collections.defaultdict(dict)
        for [e1, e2], v in zip(equations, values):
            eqs[e1][e2] = v
            eqs[e2][e1] = 1 / v
        for k in eqs:
            for i in eqs[k]:
                for j in eqs[k]:
                    eqs[i][j] = eqs[i][k] * eqs[k][j]
        return [eqs[q1].get(q2, -1) for q1, q2 in queries]
