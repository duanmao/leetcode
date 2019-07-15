// Time: O(n), space: O(n)
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> maxes;
        if (nums.empty()) return maxes; // Attention
        map<int, int> dict;
        int start = 0, end;
        for (end = 0; end < k; ++end) ++dict[nums[end]];
        while (end < nums.size()) {
            maxes.push_back(dict.rbegin() -> first);
            int key = nums[start];
            --dict[key];
            if (dict[key] == 0) dict.erase(key);
            ++start;
            ++dict[nums[end++]];
        }

        maxes.push_back(dict.rbegin() -> first); // Attention
        return maxes;
    }
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> maxes;
        map<int, int> dict;
        int start = -1, end;
        for (end = 0; end < k - 1; ++end) ++dict[nums[end]];
        while (end < nums.size()) {
            if (start >= 0) {
                int key = nums[start];
                --dict[key];
                if (dict[key] == 0) dict.erase(key);
            }
            
            ++start;
            ++dict[nums[end++]];
            maxes.push_back(dict.rbegin() -> first);
        }
        
        return maxes;
    }
};
