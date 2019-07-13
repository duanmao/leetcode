class Solution {
public:
    string countAndSay(int n) {
        if (n <= 0) return "";
        string s = "1";
        for (int i = 1; i < n; ++i) {
            string next = "";
            int count = 1;
            int len = s.length();
            for (int j = 1; j < len; ++j) {
                if (s[j] == s[j - 1]) {
                    ++count;
                } else {
                    next += to_string(count) + s[j - 1];
                    count = 1;
                }
            }
            
            next += to_string(count) + s[len - 1];
            s = next;
        }
        
        return s;
    }
};
