# Time: O(n), space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'()', '[]', '{}'}
        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            else:
                if stack and stack[-1] + c in valid:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
