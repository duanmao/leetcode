# Time: O(n), space: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i1, i2):
            nums[i1], nums[i2] = nums[i2], nums[i1]
        i = 0
        n = len(nums)
        while (i < n):
            if (not nums[i] == i + 1 and 0 < nums[i] <= n and not nums[i] == nums[nums[i] - 1]):
                swap(i, nums[i] - 1)
            else:
                i += 1
        for i in range(n):
            if (not nums[i] == i + 1):
                return i + 1
        return n + 1

# Another solution with less implementation traps but more thinking tricks
# https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
