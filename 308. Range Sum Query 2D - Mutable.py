# Better performance (init: O(mn log mn), sum and update: O(logm logn)) can be achieved with Binary
# Indexed Tree, but it's not pratical for me to fully implement it in an interview, so I'll just
# stick to this relatively worse but easier solution which I can actually write out in several
# minutes. For BIT implementation: 
# https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75870/Java-2D-Binary-Indexed-Tree-Solution-clean-and-short-17ms
class NumMatrix:
    # O(mn)
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        if (not matrix): 
            self.n = -1
            self.sums = []
            return
        self.n = len(matrix[0])
        self.sums = [[0] * self.n for i in range(self.m)]
        for i in range(self.m): self.sums[i][0] = matrix[i][0]
        for i in range(self.m):
            for j in range(1, self.n):
                self.sums[i][j] = self.sums[i][j - 1] + matrix[i][j]
        # sums[i][j]: the sum from column 0 to column j in row i

    # O(n)
    def update(self, row: int, col: int, val: int) -> None:
        if (row >= self.m or col >= self.n): return
        for j in range(col, self.n):
            self.sums[row][j] += (val - self.matrix[row][col])
        self.matrix[row][col] = val

    # O(m)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if (row1 >= self.m or col1 >= self.n or not self.sums): return 0
        sum = 0
        for i in range(row1, row2 + 1):
            sum += self.sums[i][col2] - (self.sums[i][col1 - 1] if col1 else 0)
        return sum
    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
