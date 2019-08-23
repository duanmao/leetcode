class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(si, sj):
            # The sum of the grid must be 45, as it is the sum of the distinct values from 1 to 9.
            # Each horizontal and vertical line must add up to 15, as the sum of 3 of these lines equals the sum of the whole grid.
            # The diagonal lines must also sum to 15, by definition of the problem statement.
            # Adding the 12 values from the four lines that cross the center, these 4 lines add up to 60; but they also add up to the entire grid (45), plus 3 times the middle value. This implies the middle value is 5.
            if (grid[si + 1][sj + 1] != 5): return False
            
            # a1,a2,a3
            # a4,a5,a6
            # a7,a8,a9
            
            # a1 + a5 = a3 + a6
            # a1 + a3 = a5 + a8
            # 2a1 = a6 + a8
            # therefore a6 and a8 must have the same parity
            # and since a2 + a8 = a4 + a6 = 10, thus a2, a4, a6, a8 must have the same parity
            # so a1, a3, a7, a9 must have the same parity that's opposite to a2, a4, a6, a8
            # since a1 + a2 + a3 = 15, if a1 and a3 are odd, a2 must be odd too for them to add up to an odd
            # contradicts to the fact that a1 must have opposite parity to a2
            # therefore a1, a3, a7, a9 must all be even, whereas a2, a4, a6, a8 must all be odd
            leftd = rightd = 0
            for i in [0, 2]:
                for j in [0, 2]:
                    if (grid[si + i][sj + j] % 2): return False
                    if (i == j): leftd += grid[si + i][sj + j]
                    else: rightd += grid[si + i][sj + j]
            if (leftd != 10 or rightd != 10): return False
                
            for i in range(3):
                if (sum(grid[si + i][sj:sj+3]) != 15): return False
                if (grid[si][sj + i] + grid[si + 1][sj + i] + grid[si + 2][sj + i]!= 15): return False
                
            return True
                
        
        if (not grid): return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                count += check(i, j)
        return count
