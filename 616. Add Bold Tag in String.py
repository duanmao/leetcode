# Time: O(snw) 
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        bold = [False] * len(s)
        for w in dict:
            start = s.find(w)
            while (start != -1):
                end = start + len(w)
                for i in range(start, end):
                    bold[i] = True
                start = s.find(w, start + 1) # should be start + 1 but not end... weird
        res = ""
        while (i < len(s)):
            if (bold[i]):
                res += "<b>"
                while (i < len(s) and bold[i]):
                    res += s[i]
                    i += 1
                res += "</b>"
            else:
                res += s[i]
                i += 1
        # for safety, the last if check is too easy to be forgotten, so just avoid this
        # for i in range(len(s)):
        #     if (bold[i] and (i == 0 or not bold[i - 1])):
        #         res += "<b>"
        #     elif (i and bold[i - 1] and not bold[i]):
        #         res += "</b>"
        #     res += s[i]
        # if (bold[len(s) - 1]): res += "</b>" # attention!!!
        return res

# Time: O(snw + mlogm), s: len(s), n: len(dict), w: avg_len(dict[i]), m: len(intervals)
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        if (not dict): return s
        intervals = []
        for w in dict:
            starts = [i for i in range(len(s)) if s[i:].startswith(w)]
            if (starts):
                intervals.extend([(i, i + len(w)) for i in starts])
        intervals.sort()
        merged = []
        for o, c in intervals:
            if (merged and merged[-1][1] >= o):
                merged[-1][1] = max(merged[-1][1], c)
            else:
                merged.append([o, c])
        for o, c in merged[::-1]:
            s = s[:o] + "<b>" + s[o:c] + "</b>" + s[c:]
        return s
