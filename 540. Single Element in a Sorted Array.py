# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100759/Java-Binary-Search-O(log(n))-Shorter-Than-Others
# Time: O(logn), space: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) // 2
        # our target can only appear at an even index
        # so we only need to find the first even index that is not followed by the same number
        # since we want to use low and high to get pair of indices, we cut high into half initially
        while low < high:
            mid = (low + high) // 2
            if nums[2 * mid] != nums[2 * mid + 1]: high = mid # possible targets are previous ones
            else: low = mid + 1 # up until 2 * mid + 1, all numbers are paired
        return nums[2 * low]

# another magic
# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100732/Short-compare-numsi-with-numsi1
