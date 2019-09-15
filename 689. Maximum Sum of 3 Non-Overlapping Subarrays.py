# simple sliding windows
# Time: O(n), space: O(1)
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108238/Python-o(n)-time-o(1)-space.-Greedy-solution.
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sub1sum, sub2sum, sub3sum = sum(nums[:k]), sum(nums[k:2*k]), sum(nums[2*k:3*k])
        sub1start, sub2start, sub3start = 0, k, 2 * k # current window starts
        max1sum, max2sum, max3sum = sub1sum, sub1sum + sub2sum, sub1sum + sub2sum + sub3sum
        best1, bests2, bests3 = sub1start, [sub1start, sub2start], [sub1start, sub2start, sub3start]
        while sub3start < n - k:
            sub1sum += nums[sub1start + k] - nums[sub1start]
            if (max1sum < sub1sum):
                max1sum = sub1sum
                best1 = sub1start + 1
            
            sub2sum += nums[sub2start + k] - nums[sub2start]
            if (max2sum < max1sum + sub2sum):
                max2sum = max1sum + sub2sum
                bests2 = [best1, sub2start + 1]
            
            sub3sum += nums[sub3start + k] - nums[sub3start]
            if (max3sum < max2sum + sub3sum):
                max3sum = max2sum + sub3sum
                bests3 = bests2 + [sub3start + 1]
            
            sub1start += 1
            sub2start += 1
            sub3start += 1
        return bests3

# DP
# similar to DP solution to https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Time: O(3n), space: O(3n)
# in fact, it applies to the more general question which asks for max sum of m subarrays
# then Time and space complexity will become O(mn)
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # f[i][j]: up to num[j], the max sum of i subarrays of length k
        f = [[0] * n for i in range(4)]
        # used for trace back the indices of each subarray
        indices = [[0] * n for i in range(4)]
        for i in range(1, 4):
            subsum = 0
            for j in range(n):
                subsum += nums[j]
                if j >= k: subsum -= nums[j - k]
                if j >= i * k - 1: # we need at least i * k nums to form i subarrays of length k
                    # f[i][j] is either f[i][j - 1], where we don't include nums[j] at all
                    # or we consider include nums[j] as the last element of the i-th subarray
                    # so we have the i-th subarray starting from j - k + 1, ending at j
                    # thus, other i - 1 subarrays must have ended before j - k + 1, 
                    # i.e. f[i - 1][j - k] + sum_of_subarray_ending_at_j
                    f[i][j] = max(f[i][j - 1], f[i - 1][j - k] + subsum)
                    if f[i][j] > f[i][j - 1]: # we've chosen nums[j - k + 1:j] as the i-th subarray
                        indices[i][j] = j - k + 1 # record the start index of the subarray
                    else: # we used previous results
                        indices[i][j] = indices[i][j - 1] # inherit the start index
        res = []
        # trace back the start indices of each subarray, starting from the last one, i.e. the 3rd one
        idx = indices[3][n - 1]
        for i in range(3)[::-1]:
            res.append(idx)
            idx = indices[i][idx - 1]
        return res[::-1]
