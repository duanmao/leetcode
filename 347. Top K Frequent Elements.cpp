class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> dic;
        int maxfreq = 0;
        for (int num : nums) {
            ++dic[num];
            maxfreq = max(maxfreq, dic[num]);
        }
        
        vector<vector<int>> bucket(maxfreq + 1);
        for (auto kv : dic) bucket[kv.second].push_back(kv.first);
        
        vector<int> stnums;
        for (int i = maxfreq; i >= 0 && k > 0; --i) {
            if (!bucket[i].empty()) {
                for (int num : bucket[i]) {
                    stnums.push_back(num);
                    --k;
                    if (k == 0) break;
                }
            }
        }
        
        return stnums;
    }
};
