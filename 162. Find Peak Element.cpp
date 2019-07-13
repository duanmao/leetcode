// Time: O(logN), space: O(1)
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if ((mid == 0 || nums[mid - 1] < nums[mid]) && (mid == n - 1 || nums[mid + 1] < nums[mid])) 
                return mid;
            else if (mid > 0 && nums[mid - 1] > nums[mid])
                high = mid - 1;
            else low = mid + 1;
        }
        
        return 0;
    }
};


// Time: O(n), space: O(1)
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int i, n = nums.size();
        for (i = 0; i < n; ++i) {
            if ((i == 0 || nums[i - 1] < nums[i]) && (i == n - 1 || nums[i + 1] < nums[i])) return i;
        }
        return 0;
    }
};
