class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (not matrix or not matrix[0]):
            return 0
        m = len(matrix)
        n = len(matrix[0])
        f = [ [0] * (n + 1) for i in range(m + 1) ]
        maxs = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                    maxs = max(maxs, f[i][j])
        return maxs * maxs
