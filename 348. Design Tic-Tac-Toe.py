class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row, self.col, self.diag, self.antidiag = [0] * n, [0] * n, 0, 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        p = player * 2 - 3 # player1: -1, player2: 1
        self.row[row] += p
        self.col[col] += p
        if row == col: self.diag += p
        if row + col == self.n - 1: self.antidiag += p
        if p * self.n in [self.row[row], self.col[col], self.diag, self.antidiag]:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
