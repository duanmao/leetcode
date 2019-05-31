class Solution {
public:
    unordered_map<char, int> 
        dict{ {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    
    int romanToInt(string s) {
        int num = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            if (i < n - 1 && dict[s[i]] < dict[s[i + 1]]) num -= dict[s[i]]; // subtraction
            else num += dict[s[i]];
        }
        
        return num;
    }
};
