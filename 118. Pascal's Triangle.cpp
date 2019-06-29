class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) return vector<vector<int>>(); // remember this special handle
        vector<vector<int>> rows { vector<int>{1} };
        for (int i = 0; i < numRows - 1; ++i) {
            vector<int> row {1};
            for (int j = 1; j < rows[i].size(); ++j) {
                row.push_back(rows[i][j - 1] + rows[i][j]);
            }
            
            row.push_back(1);
            rows.push_back(row);
        }
        
        return rows;
    }
};
