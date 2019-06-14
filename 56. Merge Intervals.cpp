// Time: O(NlogN), space: O(1)
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> merged;
        if (intervals.empty()) return merged;
        sort(intervals.begin(), intervals.end(), cpr);
        merged.push_back(intervals[0]);
        for (vector<int> vec : intervals) {
            if (vec[0] <= merged.back()[1]) {
                merged.back()[1] = max(vec[1], merged.back()[1]);
            } else {
                merged.push_back(vector<int>{ vec[0], vec[1] });
            }
        }
        
        return merged;
    }
    
    static bool cpr(vector<int> v1, vector<int> v2) {
        return v1[0] < v2[0];
    }
};
