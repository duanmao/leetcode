# https://leetcode.com/problems/longest-string-chain/discuss/294890/C%2B%2BJavaPython-DP-Solution
# Time: O(nlogn + nl) where n is len(words) and l is the average length of each word
# Space: O(nl)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        n = len(words)
        # f[word]: max string chain including words[i]
        f = collections.defaultdict(int)
        for word in words:
            for i in range(len(word)):
                pre = word[:i] + word[i + 1:]
                f[word] = max(f[word], f.get(pre, 0) + 1)
        return max(f.values())

# Time: O(nlogn + n^2 * l), space: O(n)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def pred(w1, w2):
            if (len(w1) != len(w2) - 1): return False
            i, n = 0, len(w1)
            while (i < n and w1[i] == w2[i]): i += 1
            while (i < n and w1[i] == w2[i + 1]): i += 1
            return i == n
            
        words.sort(key = len)
        n = len(words)
        # f[i]: max string chain including words[i]
        f = [1] * n
        for i, word in enumerate(words):
            for j in range(i + 1, n):
                if (len(words[j]) == len(word)): continue
                if (len(words[j]) > len(word) + 1): break
                if (pred(word, words[j])):
                    f[j] = max(f[j], f[i] + 1)
        return max(f)
