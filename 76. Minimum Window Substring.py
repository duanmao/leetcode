# Time: O(n), space: O(1)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = [0] * 256
        dicS = [0] * 256
        for c in t:
            dicT[ord(c)] += 1
        start = end = 0
        matched = 0
        wlen = float('inf')
        wd = ""
        while (end < len(s)):
            dicS[ord(s[end])] += 1
            if (dicS[ord(s[end])] <= dicT[ord(s[end])]):
                matched += 1
            end += 1
            if (matched == len(t)):
                while (matched == len(t)):
                    dicS[ord(s[start])] -= 1
                    if (dicS[ord(s[start])] < dicT[ord(s[start])]):
                        matched -= 1
                    start += 1
                if (end - start + 1 < wlen):
                    wlen = end - start + 1
                    wd = s[start-1:end]
        return wd

# shorter but essentially the same version:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tomatch = [0]* 256
        for c in t:
            tomatch[ord(c)] += 1
        matched = 0
        start = end = 0
        window = ""
        while (end < len(s)):
            tomatch[ord(s[end])] -= 1
            matched += tomatch[ord(s[end])] >= 0
            end += 1
            if (matched == len(t)):
                while (tomatch[ord(s[start])] < 0):
                    tomatch[ord(s[start])] += 1
                    start += 1
                if (not window or end - start < len(window)):
                    window = s[start:end]
        return window
