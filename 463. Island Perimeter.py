# Time: O(mn), space: O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if (not grid or not grid[0]):
            return 0
        peri = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (grid[i][j]):
                    peri += 4
                    if (i and grid[i - 1][j]):
                        peri -= 2
                    if (j and grid[i][j - 1]):
                        peri -= 2
        return peri
