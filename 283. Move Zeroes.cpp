class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int nonzero = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) { // Indispensable!!!
                if (nonzero != i) {
                    nums[nonzero] = nums[i];
                    nums[i] = 0;
                }
                
                ++nonzero;
            }
        }
    }
};

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                ++count;
            } else if (count) {
                nums[i - count] = nums[i];
                nums[i] = 0;
            }
        }
    }
};
