class Solution {
public:
    string dict[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> letterCombinations(string digits) {
        vector<string> combs;
        if (digits.length() == 0 || digits.find('1') != string::npos) return combs;
        generate(combs, digits, 0, "");
        return combs;
    }
    
    void generate(vector<string> &combs, string digits, int pos, string curr) {
        if (pos == digits.length()) {
            combs.push_back(curr);
            return;
        }
        
        for (int i = 0; i < dict[digits[pos] - '2'].length(); ++i) {
            generate(combs, digits, pos + 1, curr + dict[digits[pos] - '2'][i]);
        }
    }
};
