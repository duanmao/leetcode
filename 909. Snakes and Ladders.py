# BFS
# Time: O(n^2), space: O(n^2)
# https://leetcode.com/problems/snakes-and-ladders/discuss/173378/Diagram-and-BFS
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def numToRowCol(x):
            row = int((x - 1)/ n)
            col = n - 1 - (x - 1) % n if int(row % 2) else (x - 1) % n
            row = n - 1 - row
            return row, col
        
        queue = collections.deque([(1, 0)])
        added = set([1])
        while queue:
            x, s = queue.popleft()
            for i in range(1, 7):
                nx = x + i
                if nx <= n * n:
                    nr, nc = numToRowCol(nx)
                    if board[nr][nc] != -1:
                        nx = board[nr][nc]
                    if nx == n * n: return s + 1
                    if nx not in added:
                        queue.append((nx, s + 1))
                        added.add(nx)
        return -1
