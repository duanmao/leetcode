# This is essentially a Travelling Salesman Problem, which is NP-hard.
# https://leetcode.com/problems/find-the-shortest-superstring/discuss/194932/Travelling-Salesman-Problem

# https://leetcode.com/articles/find-the-shortest-superstring/
# Intuition:

# We have to put the words into a row, where each word may overlap the previous word. This is because no word is contained in any word.

# Also, it is sufficient to try to maximize the total overlap of the words.

# Say we have put some words down in our row, ending with word A[i]. Now say we put down word A[j] as the next word, where word j hasn't been put down yet. The overlap increases by overlap(A[i], A[j]).

# We can use dynamic programming to leverage this recursion. Let dp(mask, i) be the total overlap after putting some words down (represented by a bitmask mask), for which A[i] was the last word put down. Then, the key recursion is dp(mask ^ (1<<j), j) = max(overlap(A[i], A[j]) + dp(mask, i)), where the jth bit is not set in mask, and i ranges over all bits set in mask.

# Of course, this only tells us what the maximum overlap is for each set of words. We also need to remember each choice along the way (ie. the specific i that made dp(mask ^ (1<<j), j) achieve a minimum) so that we can reconstruct the answer.

# Algorithm:

# Our algorithm has 3 main components:

# 1. Precompute overlap(A[i], A[j]) for all possible i, j.
# 2. Calculate dp[mask][i], keeping track of the "parent" i for each j as described above.
# 3. Reconstruct the answer using parent information.

# Time: O(N^2 (2^N + W)), where N is the number of words, and W is the maximum length of each word.
# Space: O(N (2^N + W)).
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        if (not A): return ''
        
        # compute the overlapping length of s + t
        def overlapLen(s, t):
            m, n = len(s), len(t)
            for l in range(min(m, n), -1, -1):
                if (s.endswith(t[:l])):
                    return l
            return 0
            
        n = len(A)
        overlap = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if (i != j):
                    overlap[i][j] = overlapLen(A[i], A[j])
                    overlap[j][i] = overlapLen(A[j], A[i])
        
        totalStates = 2 ** n # each word can be chosen or not chosen, so we have 2^n states
        # maxOverlap[state][i]: the max overlap in current state (chosen words) that ends with A[i]
        maxOverlap = [[0] * n for i in range(totalStates)]
        pre = [[-1] * n for i in range(totalStates)] # path recording
        # try each state
        for s in range(1, totalStates):
            # try append A[i] to the current state
            for i in range(n):
                if (s & (1 << i)): continue # A[i] has already been used before, skip
                newS = s ^ (1 << i) # next state where A[i] is used
                # try every previous state that ends with A[j]
                for j in range(n):
                    if (s & (1 << j)): # if A[j] has been used
                        # append A[i] after A[j], so that we potentially get more overlaps
                        newOverlap = maxOverlap[s][j] + overlap[j][i]
                        # also check = is important here as two strings can have 0 overlap
                        # but we also want to record it too; with only > check, we'll miss it
                        if (newOverlap >= maxOverlap[newS][i]):
                            maxOverlap[newS][i] = newOverlap
                            pre[newS][i] = (s, j)
        
        # find the last word and reconstruct path
        maxOverlapLen = maxOverlap[totalStates - 1][0]
        cur = (totalStates - 1, 0)
        for i in range(1, n):
            # also check = is important here for the same reason as above
            if (maxOverlap[totalStates - 1][i] >= maxOverlapLen):
                maxOverlapLen = maxOverlap[totalStates - 1][i]
                cur = (totalStates - 1, i)
        nxt = -1
        res = ""
        while (True):
            state, i = cur
            if (nxt == -1): res = A[i]
            else: res = A[i][:len(A[i]) - overlap[i][nxt]] + res
            nxt = i
            cur = pre[state][i]
            if (cur == -1): break
        return res
