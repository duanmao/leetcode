// Time: O(n), space: O(1)
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero = 0, one = 0, two = nums.size() - 1;
        while (one <= two) { // = should must be included here
            if (nums[one] == 0) {
                swap(nums[one], nums[zero]);
                ++zero;
            } else if (nums[one] == 2) {
                swap(nums[one], nums[two]);
                --two;
                --one;
            }
            
            ++one;
        }
    }
};
