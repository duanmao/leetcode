# Time: initialize: O(n^2), query: O(1); Space: O(n^2)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        def getSums(matrix):
            if (not matrix): return None
            m, n = len(matrix), len(matrix[0])
            f = [[0] * n for i in range(m)]
            f[0][0] = matrix[0][0]
            for i in range(1, m): f[i][0] = f[i - 1][0] + matrix[i][0]
            for j in range(1, n): f[0][j] = f[0][j - 1] + matrix[0][j]
            for i in range(1, m):
                for j in range(1, n):
                    f[i][j] = f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1] + matrix[i][j]
            return f
            
        self.sums = getSums(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if (not self.sums): return 0
        up = self.sums[row1 - 1][col2] if row1 else 0
        left = self.sums[row2][col1 - 1] if col1 else 0
        upleft = self.sums[row1 - 1][col1 - 1] if row1 and col1 else 0
        return self.sums[row2][col2] - up - left + upleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
