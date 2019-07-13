// Time: O(mn), space:O(1)
class Solution {
public:
    int hori[4] = {-1, 1, 0, 0};
    int vert[4] = {0, 0, -1, 1};
    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;
        if (grid.empty()) return 0;
        int m = grid.size(), n = grid[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    ++islands;
                    dfs(grid, i, j);
                }
            }
        }
        
        return islands;
    }
    
    void dfs(vector<vector<char>> &grid, int row, int col) {
        if (row >= 0 && col >= 0 && row < grid.size() && col < grid[0].size() && grid[row][col] == '1') {
            grid[row][col] = '2';
            for (int i = 0; i < 4; ++i)
                dfs(grid, row + hori[i], col + vert[i]);
        }
    }
};
