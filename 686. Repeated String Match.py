# both O(n) without the substring checking part which depends on the implementation of build-in "in"
# method, if it's using KMP then it's O(m + n), otherwise can be O(mn)
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # https://leetcode.com/problems/repeated-string-match/discuss/108090/Intuitive-Python-2-liner
        times = len(B) // len(A) + bool(len(B) % len(A)) # lower bound: ceil(len(B) / len(A))
        if (B in times * A): return times
        if (B in (times + 1) * A): return times + 1 # upper bound
        return -1

# Time: O(m + n), space: O(n)
# fastest using KMP
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        m, n = len(A), len(B)
        # prefix table in KMP
        lps = [0] * n
        i, j = 1, 0
        while (i < n):
            if (B[i] == B[j]):
                lps[i] = j + 1
                i += 1
                j += 1
            else:
                if (j == 0): i += 1
                else: j = lps[j - 1]
        # use prefix table to build A
        i = j = 0
        while (j < n):
            if (i - j > m): return -1 # the start point of pattern exceeds A's length
            if (A[i % m] == B[j]):
                i += 1
                j += 1
            else:
                if (j == 0): i += 1
                else: j = lps[j - 1]
        # print(i, j)
        return i // m + bool(i % m)
