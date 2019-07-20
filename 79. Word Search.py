# Time: O(mn*4^L) where m and n are dimensions of the board and L is the length of the target word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:    
        if (not len(board)):
            return False
        m = len(board)
        n = len(board[0])
        neighs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        def dfs(visited, row, col, pos):
            if (pos == len(word)):
                return True
            if (row < 0 or row >= m or col < 0 or col >= n or visited[row][col] or
                    not board[row][col] == word[pos]):
                return False
            visited[row][col] = True
            found = False
            for i, j in neighs:
                if (dfs(visited, row + i, col + j, pos + 1)):
                    found = True
                    break
            visited[row][col] = False
            return found
            
        visited = [[False] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if (dfs(visited, i, j, 0)):
                    return True
        return False
