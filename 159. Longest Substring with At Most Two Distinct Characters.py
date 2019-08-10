# Time: O(n), space: O(1)
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = count = maxlen = 0
        mark = collections.defaultdict(int)
        for i, c in enumerate(s):
            if (not mark[c]): count += 1
            mark[c] += 1
            while (count > 2):
                mark[s[left]] -= 1
                if (not mark[s[left]]): count -= 1
                left += 1
            maxlen = max(maxlen, i - left + 1)
        return maxlen

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = right = 0
        mark = collections.defaultdict(int)
        count = 0
        maxlen = 0
        while (right < len(s)):
            if (not mark[s[right]]): count += 1
            mark[s[right]] += 1
            right += 1
            while (count > 2):
                mark[s[left]] -= 1
                if (not mark[s[left]]): count -= 1
                left += 1
            maxlen = max(maxlen, right - left)
        return maxlen
