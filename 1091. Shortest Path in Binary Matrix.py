# bfs
# O(n^2)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direcs = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i or j): direcs.append([i, j])
                    
        if (not grid): return 0
        n = len(grid)
        if (grid[0][0] == 1 or grid[n - 1][n - 1] == 1): return -1
        queue = collections.deque([((0, 0), 1)])
        added = {(0, 0)}
        while (queue):
            (curi, curj), l = queue.popleft()
            if (curi == curj == n - 1): return l
            for i, j in direcs:
                ni, nj = curi + i, curj + j
                if (0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0):
                    if ((ni, nj) not in added):
                        queue.append(((ni, nj), l + 1))
                        added.add((ni, nj))
        return -1
