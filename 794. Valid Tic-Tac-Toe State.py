class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(mark):
            if (mark * 3 in board or
                board[0][0] == board[1][0] == board[2][0] == mark or
                board[0][1] == board[1][1] == board[2][1] == mark or
                board[0][2] == board[1][2] == board[2][2] == mark or
                board[0][0] == board[1][1] == board[2][2] == mark or
                board[0][2] == board[1][1] == board[2][0] == mark):
                return True
            return False
        
        countx = sum([row.count('X') for row in board])
        counto = sum([row.count('O') for row in board])
        if countx - counto == 1: 
            # second player cannot win in this case
            return not win('O')
        elif countx == counto:
            # first player cannot win in this case
            return not win('X')
        else:
            return False
