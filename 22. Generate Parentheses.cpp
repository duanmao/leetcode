class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> prts;
        generate(n, n, "", prts);
        return prts;
    }
    
    void generate(int left, int right, string cur, vector<string> &prts) {
        if (right == 0) {
            prts.push_back(cur);
            return;
        }
        
        if (left) generate(left - 1, right, cur + "(", prts);
        if (right > left) generate(left, right - 1, cur + ")", prts);
    }
};
