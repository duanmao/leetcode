class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> counter;
        for (char c : s) counter[c]++;
        for (char c : t) {
            if (counter[c]) --counter[c];
            else return false;
        }
        
        return true;
    }
};
