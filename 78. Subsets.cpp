class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> sets;
        sets.push_back(vector<int>());
        for (int num : nums) {
            int n = sets.size();
            for (int i = 0; i < n; ++i) {
                vector<int> cp = sets[i];
                cp.push_back(num);
                sets.push_back(cp);
            }
        }
        
        return sets;
    }
};

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        return generate(nums, 0);
    }
    
    vector<vector<int>> generate(vector<int> &nums, int cur) {
        vector<int> set;
        vector<vector<int>> subsets;
        subsets.push_back(set);
        if (cur == nums.size()) return subsets;
        
        subsets = generate(nums, cur + 1);
        int n = subsets.size(); // ATTENTION!!!!!!!!!! I'M STUPID!
        
        for (int i = 0; i < n; ++i) {
            vector<int> cp = subsets[i];
            subsets.push_back(cp);
            subsets[i].push_back(nums[cur]);
        }
        
        return subsets;
    }
};
