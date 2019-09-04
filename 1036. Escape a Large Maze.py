# https://leetcode.com/problems/escape-a-large-maze/discuss/282849/Python-BFS-and-DFS-Maximum-Blocked-19900
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        direcs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        blocked = set((x, y) for x, y in blocked)
        
        def dfs(current, target, visited):
            if (current == target or len(visited) > 20000):
                return True
            curi, curj = current
            visited.add((curi, curj))
            for mi, mj in direcs:
                ni, nj = curi + mi, curj + mj
                if (0 <= ni < 10e6 and 0 <= nj < 10e6 and 
                    (ni, nj) not in blocked and (ni, nj) not in visited):
                    if (dfs([ni, nj], target, visited)): return True
            return False
        
        return dfs(source, target, set()) and dfs(target, source, set())
