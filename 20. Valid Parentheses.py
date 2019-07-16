# Time: O(n), space: O(n)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if (c in ['{', '[', '(']):
                stack.append(c)
            else:
                if (len(stack) and stack[-1] == match[c]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
