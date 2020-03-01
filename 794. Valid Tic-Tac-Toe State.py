class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        n = 3
        
        def win(mark):
            if mark * n in board: return True
            for j in range(n):
                if sum(board[i][j] == mark for i in range(n)) == n:
                    return True
            if sum(board[i][i] == mark for i in range(n)) == n:
                return True
            if sum(board[i][n - i - 1] == mark for i in range(n)) == n:
                return True
            return False
            
        countx = sum(row.count('X') for row in board)
        counto = sum(row.count('O') for row in board)
        if countx == counto: # 'X' cannot win
            return not win('X')
        elif countx - counto == 1: # 'O' cannot win
            return not win('O')
        else:
            return False
