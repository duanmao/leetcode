class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, ld, rd = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)
        
        def solve(res, sol):
            if (len(sol) == n):
                s = []
                for row, colm in enumerate(sol):
                    colm += 1
                    s.append("." * (colm - 1) + "Q" + "." * (n - colm))
                res.append(s)
                return
            row = len(sol)
            for i in range(n):
                if (not col[i] and not ld[n - (row - i) - 1] and not rd[row + i]):
                    col[i] = ld[n - 1 - (row - i)] = rd[row + i] = True
                    sol.append(i)
                    solve(res, sol)
                    sol.pop()
                    col[i] = ld[n - 1 - (row - i)] = rd[row + i] = False
                        
        res, sol = [], []
        solve(res, sol)
        return res

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(res, sol):
            if (len(sol) == n): 
                res.append(sol[:])
                return
            cur = len(sol)
            for i in range(1, n + 1):
                valid = True
                for j, x in enumerate(sol):
                    if (i == x or cur - j == abs(i - x)):
                        valid = False
                        break
                if (valid):
                    sol.append(i)
                    solve(res, sol)
                    sol.pop()
                        
        res, sol = [], []
        solve(res, sol)
        for sol in res:
            for row, col in enumerate(sol):
                sol[row] = "." * (col - 1) + "Q" + "." * (n - col)
        return res
