# Time: O(n), space: O(1)
import itertools
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process(s):
            skip = 0
            for i in range(len(s))[::-1]:
                if s[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield s[i]

        return all(x == y for x, y in itertools.zip_longest(process(S), process(T)))

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # find the index of the next char from backwards that actually stays in s
        def findNextBackwards(s, i):
            skip = 0
            while i >= 0 and (skip or s[i] == '#'):
                if s[i] == '#': skip += 1
                else: skip -= 1
                i -= 1
            return i

        i, j = len(S) - 1, len(T) - 1
        while i >= 0 or j >= 0:
            i = findNextBackwards(S, i)
            j = findNextBackwards(T, j)
            if i < 0 or j < 0:
                return i * j > 0
            else:
                if S[i] != T[j]: return False
            i -= 1
            j -= 1
        return True

# Time: O(N), space: O(N)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process(s):
            stack = []
            for c in s:
                if (c == '#'):
                    if (len(stack)): stack.pop()
                else:
                    stack.append(c)
            return stack
        
        ss, st = process(S), process(T)
        return ss == st
