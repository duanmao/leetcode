# Time: O(n), space: O(1)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT, dicS = collections.defaultdict(int), collections.defaultdict(int)
        for c in t: dicT[c] += 1
        win = ""
        start = 0
        matched = 0
        for i, c in enumerate(s):
            dicS[c] += 1
            if dicS[c] <= dicT[c]: matched += 1
            if matched < len(t):
                continue
            while matched == len(t):
                dicS[s[start]] -= 1
                if dicS[s[start]] < dicT.get(s[start]): matched -= 1
                start += 1
            if not win or i - start + 2 < len(win):
                win = s[start - 1:i + 1]
        return win

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

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = collections.defaultdict(int)
        for c in t: dicT[c] += 1
        win = ""
        dicS = collections.defaultdict(int)
        start = 0
        count = 0
        for i, c in enumerate(s):
            if c in dicT:
                dicS[c] += 1
                if dicS[c] == dicT[c]: count += 1
            if count < len(dicT):
                continue
            while count == len(dicT):
                dicS[s[start]] -= 1
                if s[start] in dicT and dicS[s[start]] < dicT[s[start]]: count -= 1
                start += 1
            if not win or i - start + 2 < len(win):
                win = s[start - 1:i + 1]
        return win
