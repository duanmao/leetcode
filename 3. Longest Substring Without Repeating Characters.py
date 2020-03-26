# Time: O(n), space: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastpos = [-1] * 256
        maxl = 0
        start = 0
        for i, c in enumerate(s):
            # if (lastpos[ord(c)] >= start): # found duplicate
            #     start = lastpos[ord(c)] + 1
            start = max(start, lastpos[ord(c)] + 1) # equivalent to above
            lastpos[ord(c)] = i
            maxl = max(maxl, i - start  + 1)
        return maxl

import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeated = collections.defaultdict(bool)
        start = 0
        maxlen = 0
        for i, c in enumerate(s):
            if not repeated[c]:
                repeated[c] = True
                continue
            maxlen = max(maxlen, i - start)
            while repeated[c]:
                repeated[s[start]] = False
                start += 1
            repeated[c] = True # remember to mark the current char
        maxlen = max(maxlen, len(s) - start)
        return maxlen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mark = [False] * 256
        start = end = 0
        maxl = 0
        while (end < len(s)):
            while (end < len(s) and not mark[ord(s[end])]):
                mark[ord(s[end])] = True
                end += 1
            maxl = max(maxl, end - start)
            if (end == len(s)):
                break
            while (start < end and not s[start] == s[end]):
                mark[ord(s[start])] = False
                start += 1
            start += 1
            end += 1 # important
        return maxl
