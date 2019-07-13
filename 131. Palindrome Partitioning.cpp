// Time: O(2^n), space: O(n^2)
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = s.length();
        vector<vector<bool> > f(n, vector<bool>(n, false));
        for (int i = 0; i < n; ++i) {
            markPalin(i, i, s, f);
            markPalin(i, i+1, s, f);
        }
        
        vector<vector<string>> parts;
        vector<string> part;
        slice(parts, part, f, s, 0);
        return parts;
    }
    
    void markPalin(int left, int right, string s, vector<vector<bool>> &f) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) f[left--][right++] = true;
    }
    
    void slice(vector<vector<string>> &parts, vector<string> &part, vector<vector<bool>> &f, string s, int start) {
        if (start == s.length()) {
            parts.push_back(part);
            return;
        }
        
        for (int i = start; i < s.length(); ++i) {
            if (f[start][i]) {
                part.push_back(s.substr(start, i - start + 1));
                slice(parts, part, f, s, i + 1);
                part.pop_back();
            }
        }
    }
};
