# BFS
# Time: O(mn), space: O(mn) though can be O(1) if modification on the input grid is okay
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        islands = 0
        
        offi = [-1, 1, 0, 0]
        offj = [0, 0, -1, 1]
        def expand(si, sj):
            q = collections.deque([(si, sj)])
            while (q):
                curi, curj = q.popleft()
                for k in range(4):
                    ni, nj = curi + offi[k], curj + offj[k]
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1' and not visited[ni][nj]:
                        visited[ni][nj] = True
                        q.append((ni, nj))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    islands += 1
                    expand(i, j)
        return islands
