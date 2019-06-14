// Time: O(n), space: O(n)
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        vector<bool> bucket(n + 1, false);
        for (int num : nums) bucket[num] = true;
        for (int i = 0; i < n + 1; ++i) if (!bucket[i]) return i;
        return -1;
    }
};

// Time: O(n), space: O(1)
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int expected = n * (n + 1) / 2;
        int sum = 0;
        for (int num : nums) sum += num;
        return expected - sum;
    }
};

// Time: O(n), space: O(1)
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int target = n;
        for (int i = 0; i < n; ++i) {
            target ^= i;
            target ^= nums[i];
        }
        
        return target;
    }
};
