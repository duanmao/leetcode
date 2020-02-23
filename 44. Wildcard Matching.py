# Time: O(mn), space: O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for i in range(m + 1)]
        f[0][0] = True
        for j in range(1, n + 1): f[0][j] = f[0][j - 1] and p[j - 1] == '*'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':
                    f[i][j] = f[i - 1][j] or f[i][j - 1]
        return f[m][n]
