# Time: O(n), space: O(n) in this implementation, but can be O(1) if we do the backward part
# manually without using the reversed string
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def longestValidPr(s, openp):
            start = 0
            openpr = 0
            maxlen = 0
            for i, c in enumerate(s):
                if (c == openp): openpr += 1
                else: openpr -= 1
                if (openpr == 0): 
                    maxlen = max(maxlen, i - start + 1)
                elif (openpr < 0): 
                    openpr = 0
                    start = i + 1
            return maxlen
        
        return max(longestValidPr(s, '('), longestValidPr(reversed(s), ')'))

# Time: O(n), space: O(n)
# https://leetcode.com/problems/longest-valid-parentheses/discuss/14355/My-solution-using-one-stack-in-one-pass
# https://leetcode.com/problems/longest-valid-parentheses/discuss/14126/My-O(n)-solution-using-a-stack
# also a 'DP' solution in the second link
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxlen = 0
        for i, c in enumerate(s):
            if (c == '('):
                stack.append(i)
            else:
                if (stack and s[stack[-1]] == '('):
                    stack.pop()
                    maxlen = max(maxlen, i - (stack[-1] if stack else -1))
                else:
                    stack.append(i)
        return maxlen
