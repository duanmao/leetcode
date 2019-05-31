class Solution {
public:
    int firstUniqChar(string s) {
        int dict[128] = { 0 }; // Initialization to 0 here is necessary
        for (char c : s) dict[c]++;
        for (int i = 0; i < s.length(); ++i) if (dict[s[i]] == 1) return i;
        return -1;
    }
};
