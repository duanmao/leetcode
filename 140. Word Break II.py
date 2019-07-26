# DFS with memorization
# Time: worst case O(2^n) where n is the length of the string
# e.g. s = "aaaaaa", dict = ['a', 'aa', ..., 'aaaaa']
# Every possible partition is a valid sentence, and there are 2^n-1 such partitions. 
# It should be clear that the algorithm cannot do better than this since it generates all valid sentences.
# Likewise, the space complexity will also be O(2^n) for the same reason - every partition is stored in memory.
# Best case is improved to be O(n^2), e.g. s = "aaaaab", dict = ["a", "aa", ..., "aaaaa"]
# O(len(wordDict) ^ len(s / minWordLenInDict))

# the 2 versions below are essentially the same, just the 1st one uses DP to do more pruning

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        visited = {}
        n = len(s)
        separable = [False] * n + [True]
        for i in range(n)[::-1]:
            for j in range(i, n):
                if (separable[j + 1] and s[i:j+1] in wordDict):
                    separable[i] = True

        def generate(s, start):
            if (start >= len(s)):
                return [""]
            elif (start in visited):
                return visited[start]
            visited[start] = []
            for i in range(start, len(s)):
                if (separable[start] and s[start:i + 1] in wordDict):
                    rest = generate(s, i + 1)
                    for st in rest:
                        if (st): visited[start].append(" ".join([s[start:i + 1], st]))
                        else: visited[start].append(s[start:i + 1])
                elif (not separable[start]):
                    break
            return visited[start]

        return generate(s, 0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        visited = {}
        
        def generate(s, start):
            if (start >= len(s)):
                return [""]
            elif (start in visited):
                return visited[start]
            visited[start] = []
            for i in range(start, len(s)):
                if (s[start:i + 1] in wordDict):
                    rest = generate(s, i + 1)
                    for st in rest:
                        if (st): visited[start].append(" ".join([s[start:i + 1], st]))
                        else: visited[start].append(s[start:i + 1])
                elif (s[start:i + 1] not in [w[:(i + 1 - start)] for w in wordDict]):
                    break
            return visited[start]
                    
        return generate(s, 0)
