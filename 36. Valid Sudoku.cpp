class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<bool>> row(9, vector<bool>(9, false)),
            column(9, vector<bool>(9, false)), grid(9, vector<bool>(9, false));
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') continue;
                int num = board[i][j] - '1';
                if (!row[i][num] && !column[j][num] && !grid[i/3 * 3 + j/3][num]) {
                    row[i][num] = true;
                    column[j][num] = true;
                    grid[i/3 * 3 + j/3][num] = true;
                } else {
                    return false;
                }
            }
        }
        
        return true;
    }
};
