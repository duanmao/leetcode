# using 4 pointers is much easier than using for loop and getting lost in deciding the ranges
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if (not len(matrix)):
            return res
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while (left < right and top < bottom):
            res.extend(matrix[top][left:right + 1])
            res.extend([matrix[i][right] for i in range(top + 1, bottom + 1)])
            res.extend([matrix[bottom][j] for j in range(left, right)[::-1]])
            res.extend([matrix[i][left] for i in range(top + 1, bottom)[::-1]])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if (left == right): # these 2 steps are special and pretty easy to get wrong
            res.extend([matrix[i][left] for i in range(top, bottom + 1)])
        elif (top == bottom): # remember these special handling 
            res.extend(matrix[top][left:right + 1])
        return res
