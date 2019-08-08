# https://leetcode.com/problems/brace-expansion-ii/discuss/317623/Python3-Clear-and-Short-Recursive-Solution
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        level = 0
        groups = [[]]
        for i, c in enumerate(expression):
            if (c == '{'):
                if (level == 0):
                    start = i + 1
                level += 1
            elif (c == '}'):
                level -= 1
                if (level == 0):
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif (c == ',' and level == 0):
                groups.append([])
            elif (level == 0):
                groups[-1].append([c])
        words = set()
        for group in groups:
            words |= set(map("".join, itertools.product(*group)))
        return sorted(words)
