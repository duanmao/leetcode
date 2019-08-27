# Two pointers
# Time: worst case O(mn), but it actually beats 97+%, empirically the fastest among the all
# Space: O(1)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        lens, lent = len(S), len(T)
        ptrs = ptrt = 0
        res = ""
        while (ptrs < lens):
            if (S[ptrs] == T[ptrt]):
                ptrt += 1
                if (ptrt == lent): # match found
                    end = ptrs
                    # move backwards to find the start
                    ptrt -= 1
                    while (ptrt >= 0):
                        while (S[ptrs] != T[ptrt]): ptrs -= 1
                        ptrt -= 1
                        ptrs -= 1 # remember
                    ptrs += 1 # remember
                    if (not res or len(res) > end - ptrs + 1):
                        res = S[ptrs:end + 1]
                    ptrt = 0
            ptrs += 1
                
        return res

# DP
# Time: O(mn) for worst case, when S is composed of all duplicates with T (same char)
# generally better than O(mn) for random cases
# Space: O(n), where m is the length of S, n is the length of T
# https://leetcode.com/problems/minimum-window-subsequence/discuss/109354/Python-O(m)-space-complexity-almost-O(n)-time-complexity
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        lens, lent = len(S), len(T)

        indices = collections.defaultdict(list)
        for i, c in enumerate(T):
            indices[c].append(i)

        # f[i]: the start index in S that contains T[:i]
        f = [-1] * lent

        res = ""
        for j, c in enumerate(S):
            if (indices.get(c)):
                # S[j] can match with some place(s) in T
                for i in indices.get(c)[::-1]:
                    if (i): f[i] = f[i - 1]
                    else: f[i] = j # i == 0, S[j] can possibly be a new starting point
                    # if T has been fully matched, update the result
                    # exclude f[i] == -1 because it means there's no match from the very beginning at all
                    if (i == lent - 1 and f[i] != -1):
                        subs = S[f[i]:j + 1]
                        if (not res or len(res) > len(subs)):
                            res = subs
        return res

# DP
# Time, space: O(mn)
# https://leetcode.com/problems/minimum-window-subsequence/discuss/109362/Java-Super-Easy-DP-Solution-(O(mn))
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        lens, lent = len(S), len(T)
        # f[i][j]: the rightmost start index in S that satisfies S[:j] contains T[:i]
        f = [[-1] * lens for i in range(lent)]

        if (S[0] == T[0]): f[0][0] = 0
        for j in range(1, lens):
            if (S[j] == T[0]): f[0][j] = j
            else: f[0][j] = f[0][j - 1]

        for i in range(1, lent):
            for j in range(1, lens):
                if (T[i] == S[j]): f[i][j] = f[i - 1][j - 1]
                else: f[i][j] = f[i][j - 1]

        # find result
        start = end = -1
        for j in range(lens):
            if (f[lent - 1][j] != -1 and
                (start == -1 or end - start > j - f[lent - 1][j])):
                start = f[lent - 1][j]
                end = j
        return S[start:end + 1]

# DP
# Time, space: O(mn)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        lens, lent = len(S), len(T)
        # f[i][j]: the min substring length of S[:j] including S[j] that contains T[:i]
        f = [[float('inf')] * lens for i in range(lent)]
        
        # initialization
        if (T[0] == S[0]): f[0][0] = 1
        for j in range(1, lens):
            if (T[0] == S[j]): f[0][j] = 1
            else: f[0][j] = f[0][j - 1] + 1
        
        # fill table
        for i in range(1, lent):
            for j in range(1, lens):
                f[i][j] = f[i][j - 1] + 1
                if (T[i] == S[j]):
                    f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
                    
        # get result
        minlen = min(f[lent - 1])
        if (minlen == float('inf')): return ""
        
        end = f[lent - 1].index(minlen)
        i, j = lent - 1, end
        while (i >= 0):
            if (i == 0 and f[i][j] == 1): break
            if (f[i][j] == f[i][j - 1] + 1):
                j -= 1
            else:
                i -= 1
                j -= 1
        return S[j:end+1]
