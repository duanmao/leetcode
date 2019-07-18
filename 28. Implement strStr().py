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
