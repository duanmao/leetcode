# https://leetcode.com/problems/number-of-matching-subsequences/solution/
# https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation/
# O(ns + m), ns: sum(len(words[i])), m: len(S)
# space: O(n), n: # of words
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        pending_char = collections.defaultdict(list)
        for w_itr in map(iter, words):
            pending_char[next(w_itr)].append(w_itr)
        for c in S:
            update = pending_char.pop(c, [])
            for w_itr in update:
                pending_char[next(w_itr, None)].append(w_itr)
        return len(pending_char[None])

# O(ns + m), ns: sum(len(words[i])), m: len(S)
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def idx(c):
            return ord(c) - ord('a')

        def buildIndices(s):
            n = len(s)
            # indices[l][c]: starting from pos l, the position of the next char c
            indices = [[-1] * 26 for i in range(n)]
            for i in range(n)[::-1]:
                if (i < n - 1): indices[i] = indices[i + 1][:]
                indices[i][idx(s[i])] = i
            return indices

        indices = buildIndices(S)
        count = 0
        for w in words:
            count += 1
            pos = 0
            for i, c in enumerate(w):
                if (indices[0][idx(c)] == -1 or
                    pos >= len(S) or indices[pos][idx(c)] == -1):
                    count -= 1
                    break
                pos = indices[pos][idx(c)] + 1
        return count

# TLE
# O(ns + 26m), n is the number of words, s is the avg length or words, m is len(S)
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def buildIndices(s):
            n = len(s)
            indices = {}
            for i, c in enumerate(s):
                if (c not in indices): indices[c] = [-1] * n
                indices[c][i] = i
            for c in indices:
                for i in range(n - 1)[::-1]:
                    if (indices[c][i] == -1): indices[c][i] = indices[c][i + 1]
            return indices
                        
        indices = buildIndices(S)
        count = 0
        for w in words:
            count += 1
            pos = 0
            for i, c in enumerate(w):
                if (c not in indices or pos >= len(S) or indices[c][pos] == -1):
                    count -= 1
                    break
                pos = indices[c][pos] + 1
        return count
