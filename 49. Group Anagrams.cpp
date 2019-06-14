// Time: O(nlogL), space: O(n)
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dict;
        for (string str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            dict[key].push_back(str);
        }
        
        vector<vector<string>> grouped;
        for (auto kv: dict) grouped.push_back(kv.second);
        return grouped;
    }
};
