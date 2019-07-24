# TimeL O(n), space: O(1)
# https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if (not nums or len(nums) == 1):
            return nums[0] if nums else 0
        maxpro = minpro = res = nums[0]
        for i in range(1, len(nums)):
            # depends on whether num is positive or negative
            prevmax = maxpro
            maxpro = max(prevmax * nums[i], minpro * nums[i], nums[i])
            minpro = min(minpro * nums[i], prevmax * nums[i], nums[i])
            res = max(res, maxpro)
        return res

# Time: O(n), space: O(1)
# https://leetcode.com/problems/maximum-product-subarray/discuss/48448/A-O(n)-solution-though-not-as-great-as-answer-provided-by-Leetcode
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpro = float('-inf')
        fwdpro = 1
        bwdpro = 1
        n = len(nums)
        for i in range(n):
            fwdpro *= nums[i]
            bwdpro *= nums[n - i - 1]
            maxpro = max(maxpro, fwdpro, bwdpro)
            if not fwdpro:
                fwdpro = 1
            if not bwdpro:
                bwdpro = 1
        return maxpro
