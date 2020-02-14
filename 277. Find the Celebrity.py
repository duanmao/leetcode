# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# Time: O(n), space: O(1)
# https://leetcode.com/problems/find-the-celebrity/discuss/71227/Java-Solution.-Two-Pass
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        # Up until now, we've made sure that the candidate:
        # 1. knows no one after him (i > candidate)
        # 2. no one before him (i < candidate) knows no one
        # thus, we only need to check for this candidate:
        # 1. whether everyone after him (i > candidate) knows him
        # 2. whether everyone before him (i < candidate) knows him, and he knows none of them
        for i in range(n):
            if i < candidate and (knows(candidate, i) or not knows(i, candidate)): return -1
            elif i > candidate and not knows(i, candidate): return -1
        return candidate

# Check https://leetcode.com/problems/find-the-celebrity/discuss/71240/AC-Java-solution-using-stack
# or https://leetcode.com/problems/find-the-celebrity/discuss/71255/Share-my-two-pointer-solution
# for better understanding
