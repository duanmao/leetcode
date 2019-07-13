// Time: O(mnn), space: O(mn)
// DP + DFS
class Solution {
public:
    int offi[4] = {-1, 1, 0, 0};
    int offj[4] = {0, 0, -1, 1};
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty()) return 0;
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> lens(m, vector<int>(n, 0));
        int maxlen = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int len = dfs(matrix, lens, i, j, INT_MIN);
                maxlen = max(maxlen, len);
            }
        }
        
        return maxlen;
    }
    
    int dfs(vector<vector<int>>& matrix, vector<vector<int>> &lens, int row, int col, int pre) {
        if (row < 0 || col < 0 || row >= matrix.size() || col >= matrix[0].size() || matrix[row][col] <= pre) return 0;
        if (lens[row][col] > 0) return lens[row][col];
        int maxNextLen = 0;
        for (int k = 0; k < 4; ++k) {
            maxNextLen = max(maxNextLen, dfs(matrix, lens, row + offi[k], col + offj[k], matrix[row][col]));
        }
        
        lens[row][col] = maxNextLen + 1;
        return lens[row][col];
    }
};
