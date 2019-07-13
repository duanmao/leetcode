// Time: O(mn), space: O(1)
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.empty()) return;
        int m = matrix.size(), n = matrix[0].size();
        bool zeroRow1 = false, zeroCol1 = false;
        for (int i = 0; i < m; ++i) {
            if (matrix[i][0] == 0) {
                zeroRow1 = true;
                break;
            }
        }
        
        for (int j = 0; j < n; ++j) {
            if (matrix[0][j] == 0) {
                zeroCol1 = true;
                break;
            }
        }
        
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
            }
        }
        
        if (zeroRow1) for (int i = 0; i < m; ++i) matrix[i][0] = 0;
        if (zeroCol1) for (int j = 0; j < n; ++j) matrix[0][j] = 0;
    }
};
