// Time: O(nlogk), space: O(n)
// where k is the target length, which is of the longest subsequence
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> smallestInLen; // an array whose indices correspond to length of
        // increasing subsequence, and the values store the smallest numbers that the 
        // subsequences of corresponding lengths could end with
        // Therefore, this array should be in ascending order
        for (int i = 0; i < nums.size(); ++i) {
            // Thus, for each number in nums, we can find whether it can be a smaller
            // replacement of any exisitng elements in $smallestInLen$, with binary
            // search: if smallestInLen[j - 1] < nums[i] < smallestInLen[j], nums[i]
            // is a better candidate for length j since it's smaller, which opens 
            // more possibility of reaching at a longer subsequence
            // Otherwise, nums[i] is larger than all existing entries in $smallestInLen$,
            // then it qualifies as the ending of a longer subsequence than all the
            // existing ones, i.e. we can have one more entry in $smallestInLen$
            int pos = bisearch(smallestInLen, nums[i]);
            if (pos >= 0 && pos < smallestInLen.size()) smallestInLen[pos] = nums[i];
            else smallestInLen.push_back(nums[i]);
        }
        
        return smallestInLen.size();
    }
    
    // Find the index (i.e. length) of the 
    int bisearch(vector<int> nums, int target) {
        int low = 0, high = nums.size() - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        
        return low;
    }
};

// Time: O(n^2), space: O(n)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) return 0;
        int n = nums.size();
        vector<int> lens(n, 1);
        int maxlen = 1;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j]) lens[i] = max(lens[i], lens[j] + 1);
                maxlen = max(lens[i], maxlen);
            }
        }

        return maxlen;
    }
};
