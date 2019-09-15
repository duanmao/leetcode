# Time: O(n), space: O(1)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = collections.defaultdict(int)
        maxlen = 0
        count = 0
        start = 0
        for i, c in enumerate(s):
            if (not seen[c]): count += 1
            seen[c] += 1
            while (count > k):
                seen[s[start]] -= 1
                if (seen[s[start]] == 0): count -= 1
                start += 1
            maxlen = max(maxlen, i - start + 1)
        return maxlen
