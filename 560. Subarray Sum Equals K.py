# Time: O(n), space: O(n)
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        sums = collections.defaultdict(int)
        sums[0] = 1 # important
        add = 0
        for num in nums:
            add += num
            count += sums[add - k]
            sums[add] += 1 # must be after count update, otherwise consider case {nums = [1], k = 0}
        return count


# Brute force. Time: O(n^2), space: O(1)
# TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            add = 0
            for j in range(i, n):
                add += nums[j]
                if add == k: count += 1
        return count
