# O(ns) where n is the number of strings in the dictionary, s is the length of the target string s
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def match(longer, shorter):
            ptr = 0
            for c in longer:
                if (c == shorter[ptr]):
                    ptr += 1
                    if (ptr == len(shorter)): break
            return ptr == len(shorter)
        
        sub = ""
        for w in d:
            if (match(s, w) and len(w) >= len(sub)):
                if (len(w) > len(sub)): sub = w
                else: sub = min(w, sub)
        return sub
