# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/92242/ConciseEasy-to-understand-Java-5ms-solution-with-Explaination
# Time: O((logn)^2) or more specifically, O(logk * logn)? 
# Space: O(1)
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countStep(start, end):
            step = 0
            while start <= n:
                step += min(end, n + 1) - start
                start *= 10
                end *= 10
            return step
            
        cur = 1
        k -= 1
        while k:
            steps = countStep(cur, cur + 1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
