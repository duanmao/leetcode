class Solution {
public:
    int titleToNumber(string s) {
        int col = 0;
        // The () surrounds (c - 'A') is necessary!
        for (char c : s) col = col * 26 + (c - 'A') + 1;
        return col;
    }
};
