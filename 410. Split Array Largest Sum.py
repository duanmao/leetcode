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

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(tsum):
            k = 1
            subsum = 0
            for num in nums:
                subsum += num
                if (subsum > tsum):
                    k += 1
                    subsum = num
            return k
        
        low, high = max(nums), sum(nums)
        while (low < high):
            mid = (low + high) // 2
            k = split(mid)
            if (k > m): low = mid + 1
            else: high = mid
        return high

# Time: O(mn^2), space: O(mn)
# DP
# generalize to all kinds of inputs, but TLE in python for this case
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        # f[i + 1][j]: the min subarray sum for nums[0-i] split to j arrays
        f = [[0] * (m + 1)] + [[float('inf')] * (m + 1) for i in range(n)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cursum = nums[i - 1]
                for k in range(i)[::-1]:
                    f[i][j] = min(f[i][j], max(f[k][j - 1], cursum))
                    cursum += nums[k - 1]
        return f[n][m]

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
