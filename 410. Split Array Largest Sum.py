# Time: O(nlogm) where m is the sum of the array, space: O(1)
# Binary search + Greedy
# takes advantange of all nums are non-negative
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(lessthan):
            count = accu = 0
            for num in nums:
                accu += num
                if (accu > lessthan):
                    count += 1
                    accu = num
            return count + 1
            
        low, high = max(nums), sum(nums)
        while (low <= high):
            mid = (low + high) // 2
            count = split(mid)
            if (count <= m):
                high = mid - 1
            else:
                low = mid + 1
        return low

# Time: O(mn^2), space: O(mn)
# DP
# generalize to all kinds of inputs, but TLE in python for this case
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def dp(sums, memo, start, m):
            if (m == 1): return sums[start]
            if (memo[m][start] > 0): return memo[m][start]
            minSum = float('inf')
            curSum = 0
            for i in range(start, len(nums) - m + 1):
                curSum += nums[i]
                minSum = min(minSum, max(curSum, dp(sums, memo, i + 1, m - 1)))
            memo[m][start] = minSum
            return minSum

        if (not nums): return 0
        n = len(nums)
        sums = [0] * (n - 1) + [nums[n - 1]]
        for i in range(n - 1)[::-1]:
            sums[i] = sums[i + 1] + nums[i]
        memo = [[0] * n for i in range(m + 1)]
        return dp(sums, memo, 0, m)
