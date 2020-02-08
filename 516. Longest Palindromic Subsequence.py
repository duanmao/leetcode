# Time: O(n^2), space: O(n^2)
# DP: f[i][j]: length of the longest palindromic subsequence within s[i:j]
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for i in range(n)]
        for l in range(n):
            for i in range(n - l):
                j = i + l
                if i == j: f[i][j] = 1
                elif s[i] == s[j]: f[i][j] = f[i + 1][j - 1] + 2
                else: f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]
