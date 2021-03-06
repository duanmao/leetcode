# https://leetcode.com/articles/longest-repeating-substring/
# Binary search + set
# Time: O(nlogn), space: O(n^2)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        def check(l):
            seen = set()
            for i in range(n - l + 1): #
                cur = S[i:i + l]
                if cur not in seen: seen.add(cur)
                else: return True
            return False
        
        low, high = 1, n
        while low <= high:
            midL = (low + high) // 2
            if check(midL):
                low = midL + 1
            else:
                high = midL - 1
        return high

# DP
# Time: O(n ^ 2), space: O(n^2)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        f = [[0] * (n + 1) for i in range(n + 1)]
        maxlen = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if S[i - 1] == S[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    maxlen = max(maxlen, f[i][j])
        return maxlen

# Time: O(n^2), space: O(n)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        f = [0] * (n + 1)
        maxlen = 0
        for i in range(1, n + 1):
            for j in range(i - 1, 0, -1):
                if S[i - 1] == S[j - 1]:
                    f[j] = f[j - 1] + 1
                    maxlen = max(maxlen, f[j])
                else:
                    f[j] = 0
        return maxlen
