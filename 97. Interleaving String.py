# Time: O(mn), space: O(mn)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if (not m + n == len(s3)): return False
        f = [[False] * (n + 1) for i in range(m + 1)]
        f[0][0] = True
        for i in range(1, m + 1):
            f[i][0] = f[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            f[0][j] = f[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = (f[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                        (f[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return f[m][n]
