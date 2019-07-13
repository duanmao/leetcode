// Time: O(n^2), space: O(n^2)
class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<vector<bool>> palin(n, vector<bool>(n, false));
        for (int i = 0; i < n; ++i) {
            markPalin(s, i, i, palin);
            markPalin(s, i, i+1, palin);
        }
        
        vector<int> cuts(n, INT_MAX);
        for (int i = 0; i < n; ++i) if (palin[0][i]) cuts[i] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (palin[i + 1][j] && cuts[i] != INT_MAX) cuts[j] = min(cuts[j], cuts[i] + 1);
            }
        }
        
        return cuts[n - 1];
    }
    
    void markPalin(string s, int left, int right, vector<vector<bool>> &palin) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) palin[left--][right++] = true;
    }
};
