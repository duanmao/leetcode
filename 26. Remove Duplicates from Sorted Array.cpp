// Time: O(n), space: O(1)
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int ptr = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i - 1]) nums[ptr++] = nums[i];
        }
        
        return ptr;
    }
};
