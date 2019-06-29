// Time: O(mn), space: O(1)
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        if (board.empty() || board[0].empty()) return;
        int m = board.size(), n = board[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int count = 0;
                for (int k = max(0, i - 1); k < min(i + 2, m); ++k) {
                    for (int l = max(0, j - 1); l < min(j + 2, n); ++l) {
                        count += board[k][l] > 1 ? (board[k][l] - 2) : board[k][l];
                    }
                }
                
                if (count == 3 || count - board[i][j] == 3) board[i][j] += 2;
            }
        }
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                board[i][j] = board[i][j] > 1 ? 1 : 0;
            }
        }
    }
};
