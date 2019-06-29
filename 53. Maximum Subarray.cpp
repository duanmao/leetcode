// Time: O(n), space: O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxs = INT_MIN;
        int s = 0;
        for (int num : nums) {
            s += num;
            maxs = max(s, maxs);
            s = max(s, 0);
        }
        
        return maxs;
    }
};
