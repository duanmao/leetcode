// Time: O(n*sqrt(n)), space: O(n)
class Solution {
public:
    int numSquares(int n) {
        vector<int> f(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            int sqrs = INT_MAX;
            for (int j = 1; j * j <= i; ++j) {
                sqrs = min(sqrs, f[i - j * j] + 1);
            }

            f[i] = sqrs;
        }
        
        return f[n];
    }
};
