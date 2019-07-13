class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        for (int num : nums) s.insert(num);
        int maxlen = 0;
        while (!s.empty()) {
            int len = 0;
            int pick = *s.begin();
            int left = pick, right = pick + 1;
            while (s.count(left) > 0) {
                ++len;
                s.erase(left--);
            }
            
            while (s.count(right) > 0) {
                ++len;
                s.erase(right++);
            }
            
            maxlen = max(maxlen, len);
        }
        
        return maxlen;
    }
};
