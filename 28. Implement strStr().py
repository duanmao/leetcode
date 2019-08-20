# Time: O(mn), space: O(1)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not needle):
            return 0
        for i in range(len(haystack) - len(needle) + 1): # range is important
            for j, h in enumerate(needle):
                if (not h == haystack[i + j]):
                    break
                if (j == len(needle) - 1):
                    return i
        return -1

# Time: O(m + n), space: O(n)
# But it's actually much slower than the previous one on OJ, surprisingly
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP
        m, n = len(haystack), len(needle)
        lps = [0] * n # longest proper suffix
        i, j = 1, 0
        while (i < n):
            if (needle[i] == needle[j]):
                lps[i] = j + 1
                i += 1
                j += 1
            else:
                if (j == 0): i += 1
                else: j = lps[j - 1]
        i = j = 0
        while (i < m and j < n):
            if (haystack[i] == needle[j]):
                i += 1
                j += 1
            else:
                if (j == 0): i += 1
                else: j = lps[j - 1]
        return i - n if j == n else -1
        
# This will find all occurances of the substring
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (not needle): return 0
        # KMP
        m, n = len(haystack), len(needle)
        lps = [0] * n # longest proper suffix
        i, j = 1, 0
        while (i < n):
            if (needle[i] == needle[j]):
                lps[i] = j + 1
                i += 1
                j += 1
            else:
                if (j == 0): i += 1
                else: j = lps[j - 1]
        i = j = 0
        occur = [] # record all start points of the substring
        while (i < m):
            if (haystack[i] == needle[j]):
                i += 1
                j += 1
            else:
                if (j == 0): i += 1
                else: j = lps[j - 1]
            if (j == n):
                occur.append(i - j)
                j = lps[j - 1]
        print(occur)
        return occur[0] if occur else -1
