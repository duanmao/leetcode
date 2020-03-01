# Binary Search + hashset
# Time: O(nlogn), space: O(n^2)
# MLE
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        def check(l):
            seen = set()
            for i in range(n - l + 1): #
                cur = S[i:i + l]
                if cur not in seen: seen.add(cur)
                else: return cur
            return None

        low, high = 1, n
        res = ""
        while low <= high:
            midL = (low + high) // 2
            ds = check(midL)
            if ds:
                low = midL + 1
                res = ds
            else:
                high = midL - 1
        return res

# DP
# Time: O(n^2), space: O(n^2)
# MLE
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        f = [[0] * (n + 1) for i in range(n + 1)]
        maxlen = 0
        res = ""
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if S[i - 1] == S[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    if f[i][j] > maxlen:
                        maxlen = f[i][j]
                        res = S[i - maxlen:i]
        return res

# DP, cut space to O(n), TLE
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        f = [0] * (n + 1)
        maxlen = 0
        res = ""
        for i in range(1, n + 1):
            for j in range(i - 1, 0, -1):
                if S[i - 1] == S[j - 1]:
                    f[j] = f[j - 1] + 1
                    if f[j] > maxlen:
                        maxlen = f[j]
                        res = S[i - maxlen:i]
                else:
                    f[j] = 0
        return res
