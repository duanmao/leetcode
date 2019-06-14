// Binary search
// Time: O(nlog(max-min)), space: O(1)
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        long low = matrix[0][0], high = matrix[n - 1][n - 1];
        while (low < high) {
            long mid = (low + high) / 2;
            int count = 0;
            for (auto nums : matrix) {
                int lessthanCount = upper_bound(nums.begin(), nums.end(), mid) - nums.begin();
                count += lessthanCount;
            }
            
            if (count < k) low = mid + 1;
            else high = mid;
        }
        
        return high;
    }
};
