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
        i, j = len(S) - 1, len(T) - 1
        backs = backt = 0
        
        # find the next character from backwards that actually stays in s
        def process(s, i, back):
            while (i >= 0 and (back or s[i] == '#')):
                if (s[i] == '#'): back += 1
                else: back -= 1
                i -= 1
            return i, back
            
        while (i >= 0 or j >= 0): # must be "or" here
            i, backs = process(S, i, backs)
            j, backt = process(T, j, backt)
            if (i >= 0 and j >= 0 and S[i] == T[j]):
                i -= 1
                j -= 1
            elif (i >= 0 or j >= 0): # must be "or" too
                return False
        return i < 0 and j < 0

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
