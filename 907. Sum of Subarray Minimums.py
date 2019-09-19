# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution
# monotonic stack
# Time: O(n), space: O(n)
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        A.append(0) # a trick to avoid extra handling code after completing the for loop, relies on A[i] > 0
        stack = [] # [index of the min element so far]
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                j = stack.pop()
                left = stack[-1] if stack else -1
                res += A[j] * (j - left) * (i - j)
            stack.append(i)
        return res % (10 ** 9 + 7)

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left, right = [0] * n, [0] * n
        stack = [] # [(A[i], eligible_subarray_length)]
        for i, a in enumerate(A):
            sublen = 1
            while stack and stack[-1][0] > a:
                sublen += stack.pop()[1]
            left[i] = sublen
            stack.append((a, sublen))
        stack = []
        for i in range(n)[::-1]:
            sublen = 1
            while stack and stack[-1][0] >= A[i]:
                sublen += stack.pop()[1]
            right[i] = sublen
            stack.append((A[i], sublen))
        return sum([A[i] * left[i] * right[i] for i in range(n)]) % (10 ** 9 + 7)
