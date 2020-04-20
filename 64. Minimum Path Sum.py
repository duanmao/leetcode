# Time: O(mn), space: O(mn)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        pathSum = grid[:]
        for i in range(1, m): pathSum[i][0] += pathSum[i - 1][0]
        for j in range(1, n): pathSum[0][j] += pathSum[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                pathSum[i][j] += min(pathSum[i - 1][j], pathSum[i][j - 1])
        return pathSum[m - 1][n - 1]
