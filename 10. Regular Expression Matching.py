# Time: O(mn) where m, n are the lengths of the string and pattern
# Space: O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for i in range(m + 1)]
        f[0][0] = True
        for j in range(2, n + 1): f[0][j] = f[0][j - 2] and p[j - 1] == '*'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Attention it's *j - 2* here when * is used as empty matching!
                    # same as in the initialization above
                    f[i][j] = f[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        f[i][j] = f[i][j] or f[i - 1][j]
        return f[m][n]
