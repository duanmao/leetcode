# DFS or BFS
# Time: O(mn), space: O(mn)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if (not board or not board[0]): return
        m = len(board)
        n = len(board[0])
        hori = [-1, 1, 0, 0]
        vert = [0, 0, -1 ,1]
        
        def dfs(immu, row, col):
            immu.add((row, col))
            for k in range(4):
                i = row + hori[k]
                j = col + vert[k]
                if (0 <= i < m and 0 <= j < n and board[i][j] == "O" and (i, j) not in immu):
                    dfs(immu, i, j)
        
        immu = set()
        for i in range(m):
            if (board[i][0] == "O" and (i, 0) not in immu): dfs(immu, i, 0)
            if (board[i][n - 1] == "O" and (i, n - 1) not in immu): dfs(immu, i, n - 1)
        for j in range(n):
            if (board[0][j] == "O" and (0, j) not in immu): dfs(immu, 0, j)
            if (board[m - 1][j] == "O" and (m - 1, j) not in immu): dfs(immu, m - 1, j)
        for i in range(m):
            for j in range(n):
                if (board[i][j] == "O" and (i, j) not in immu):
                    board[i][j] = "X"
