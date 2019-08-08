# Time: O(n^2), space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if (f[j] and s[j:i] in wordDict):
                    f[i] = True
                    break
        return f[len(s)]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [True] + [False] * n
        for i in range(n):
            for j in range(i + 1, n + 1):
                w = s[i:j]
                if (f[i] and w in wordDict):
                    f[j] = True
        return f[n]

# Time: O(nm) where m is the size of the dict, space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                start = i - len(word)
                if (s[start:i] == word and start >= 0 and f[start]):
                    f[i] = True
                    break
        return f[len(s)]
