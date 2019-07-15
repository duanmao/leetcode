// Time: O(n), space: O(1) 
class Solution {
public:
    int longestSubstring(string s, int k) {
        int maxlen = 0;
        for (int i = 1; i <= 26 && i <= s.length(); ++i) {
            maxlen = max(maxlen, longestSubstrWithNUniqueChars(s, k, i));
        }

        return maxlen;
    }

    int longestSubstrWithNUniqueChars(string s, int k, int n) {
        int unique = 0, noLessThanK = 0;
        int count[26] = {0};
        int start = 0, end = 0;
        int maxlen = 0;
        while (end < s.length()) {
            if (unique <= n) {
                int idx = s[end] - 'a';
                ++count[idx];
                if (count[idx] == 1) ++unique;
                if (count[idx] == k) ++noLessThanK;
                ++end;
            } else {
                int idx = s[start] - 'a';
                --count[idx];
                if (count[idx] == 0) --unique;
                if (count[idx] == k - 1) --noLessThanK;
                ++start;
            }

            if (unique == n && noLessThanK == n) maxlen = max(maxlen, end - start);
        }

        return maxlen;
    }
};

// The idea of this one is pretty similar to the last one, both using Divide & Conquer,
// but this implementation runs much much faster, like literally "much much",
// pretty much the same as the previous one whose time complexity is strictly O(n).
// So I'm not sure about the complexity for this one now...
// The original author states it's O(n), but I'm not confident enough to confirm it
// Although empirically it's indeed extraordinarily comparable to O(n)
// space: O(1)
class Solution {
public:
    int longestSubstring(string s, int k) {
        return longest(s, k, 0, s.length() - 1);
    }
    
    int longest(string s, int k, int first, int last) {
        if (last - first + 1 < k) return 0;
        int count[26] = {0};
        for (int i = first; i <= last; ++i) ++count[s[i] - 'a'];
        
        int max_len = 0;
        for (int j = first; j <= last;) {
            while (j <= last && count[s[j]-'a'] < k) ++j;
            if (j > last) break;
            int l = j;
            while (l <= last && count[s[l]-'a'] >= k) ++l;
            //all chars appear more than k times
            if (j == first && l > last) return l-j; 
            max_len = max(max_len, longest(s, k, j, l - 1));
            j = l;
        }
        
        return max_len;
    }
};

// Time: O(n^2) worst case ? not sure
class Solution {
public:
    int longestSubstring(string s, int k) {
        return longest(s, k, 0, s.length() - 1);
    }
    
    int longest(string s, int k, int first, int last) {
        if (last - first + 1 < k) return 0;
        int count[26] = {0};
        for (int i = first; i <= last; ++i) ++count[s[i] - 'a'];
        for (int i = first; i <= last; ++i) {
            if (count[s[i] - 'a'] < k) {
                return max(longest(s, k, first, i - 1), longest(s, k, i + 1, last));
            }
        }
        
        return last - first + 1;
    }
};
