class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def stretch(t, w): # t as target
            ptr = 0
            count = 0
            for i, c in enumerate(t):
                if (ptr < len(w) and c == w[ptr]):
                    ptr += 1
                else:
                    if ((i > 1 and t[i] == t[i - 1] == t[i - 2]) or 
                       (i and i < len(t) - 1 and t[i - 1] == t[i] == t[i + 1])):
                        # if it's in the middle or at the end of at least 3 same chars
                        continue
                    else:
                        return False
            return ptr == len(w)
        
        count = 0
        for word in words:
            if (stretch(S, word)): count += 1
        return count
