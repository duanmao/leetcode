# O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (2 * s)[1:-1]

# though O(n), but much slower than the previous one
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # KMP prefix array
        p = [0] * n
        i, j = 1, 0
        while (i < n):
            if (s[i] == s[j]):
                p[i] = j + 1
                i += 1
                j += 1
            elif (j == 0):
                i += 1
            else:
                j = p[j - 1]
        return p[n - 1] and p[n - 1] % (n - p[n - 1]) == 0
