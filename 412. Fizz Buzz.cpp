class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> strs;
        for (int i = 1; i <= n; ++i) {
            string s = "";
            if (i % 3 == 0) s += "Fizz";
            if (i % 5 == 0) s += "Buzz";
            strs.push_back(s.length() ? s : to_string(i));
        }
        
        return strs;
    }
};
