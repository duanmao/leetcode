// Time: O(n), space: O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict;
        for (int i = 0; i < nums.size(); ++i) {
            if (dict.find(nums[i]) != dict.end()) return vector<int>{dict[nums[i]], i};
            else dict[target - nums[i]] = i;
        }

        return vector<int>();
    }
};

// Time: O(nlogn), space: O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> nis;
        int n = nums.size();
        for (int i = 0; i < n; ++i) nis.push_back(pair<int, int>{nums[i], i});
        sort(nis.begin(), nis.end(), comp);
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int s = nis[left].first + nis[right].first;
            if (s == target) return vector<int>{nis[left].second, nis[right].second};
            else if (s < target) ++left;
            else --right;
        }
        
        return vector<int>();
    }
    
    static bool comp(pair<int, int> p1, pair<int, int> p2) {
        return p1.first < p2.first;
    }
};
