class Solution {
public:
    Solution(vector<int>& nums) {
        this -> nums = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        vector<int> ori = nums;
        return ori;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> shuffled = reset();
        int n = nums.size();
        for (int i = 0; i < n - 1; ++i) {
            int index = rand() % (n - i);
            int x = shuffled[i];
            shuffled[i] = shuffled[i + index];
            shuffled[i + index] = x;
        }
        
        return shuffled;
    }

private:
    vector<int> nums;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
