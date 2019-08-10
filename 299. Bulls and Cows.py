# Time: O(n), space: O(1)
# two passes
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        count = [0] * 10
        for i in range(len(secret)):
            if (secret[i] == guess[i]):
                bulls += 1
            else:
                count[ord(secret[i]) - ord('0')] += 1
        for i, c in enumerate(guess):
            if (i < len(secret) and secret[i] == c): continue
            if (count[ord(c) - ord('0')]):
                cows += 1
                count[ord(c) - ord('0')] -= 1
        return str(bulls) + "A" + str(cows) + "B"

# one pass
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        count = [0] * 10
        for s, g in zip(secret, guess):
            if (s == g):
                bulls += 1
            else:
                if (count[ord(s) - ord('0')] < 0): cows += 1
                if (count[ord(g) - ord('0')] > 0): cows += 1
                count[ord(s) - ord('0')] += 1
                count[ord(g) - ord('0')] -= 1
        return str(bulls) + "A" + str(cows) + "B"
                
# fancier and empirically faster (for no reason)
from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dicts, dictg = Counter(secret), Counter(guess)
        bulls = sum(s == g for s, g in zip(secret, guess))
        return '%sA%sB' % (bulls, sum((dicts & dictg).values()) - bulls)
