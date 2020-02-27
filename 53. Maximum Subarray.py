class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, subsum = float('-inf'), 0
        for num in nums:
            subsum += num
            # updating maxsum must follow the addition to subsum
            # it cannot be placed after the reset of subsum to 0
            # otherwise it'll fail for case like nums = [-1]
            maxsum = max(maxsum, subsum)
            subsum = max(0, subsum)
        return maxsum
