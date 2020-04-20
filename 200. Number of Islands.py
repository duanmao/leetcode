# BFS
# Time: O(mn), space: O(mn) though can be O(1) if modification on the input grid is okay
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c, visited):
            move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            queue = deque([(r, c)])
            visited[r][c] = True
            while queue:
                i, j = queue.popleft()
                for offi, offj in move:
                    newi, newj = i + offi, j + offj
                    if (0 <= newi < m and 0 <= newj < n and
                        not visited[newi][newj] and grid[newi][newj] == '1'):
                        visited[newi][newj] = True
                        queue.append((newi, newj))

        if not grid: return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    bfs(i, j, visited)
        return count

# Union Find
# Time: O(mn), space: O(mn)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        parent = {}
        self.count = sum(l.count('1') for l in grid)

        def find(x):
            if x not in parent: parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py: self.count -= 1
            parent[px] = py

        move = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for mi, mj in move:
                        ni, nj = i + mi, j + mj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                            union(i * n + j, ni * n + nj)
        return self.count

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0
        m, n = len(grid), len(grid[0])

        def expand(row, col):
            if 0 <= row < m and 0 <= col < n and grid[row][col] == '1':
                grid[row][col] = '0'
                for mr, mc in move:
                    expand(row + mr, col + mc)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    expand(i, j)
        return islands
