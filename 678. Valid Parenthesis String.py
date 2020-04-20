# Time: O(n), space: O(1)
# https://leetcode.com/problems/valid-parenthesis-string/solution/ Approach 3
# https://leetcode.com/problems/valid-parenthesis-string/discuss/107577/Short-Java-O(n)-time-O(1)-space-one-pass
class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = maxLeft = 0
        for c in s:
            if c == '(':
                minLeft += 1
                maxLeft += 1
            elif c == ')':
                maxLeft -= 1
                minLeft -= 1
            else:
                minLeft -= 1 # use * as )
                maxLeft += 1 # use * as (
            if maxLeft < 0: return False
            minLeft = max(minLeft, 0)
        return minLeft == 0
