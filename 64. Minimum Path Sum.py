# Time: O(mn), space: O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        f = [[0] * n for i in range(m)]
        f[0][0] = grid[0][0]
        for i in range(1, m): f[i][0] = f[i - 1][0] + grid[i][0]
        for j in range(1, n): f[0][j] = f[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]
        return f[m - 1][n - 1]
