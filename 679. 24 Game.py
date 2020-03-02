# Time and space: O(1)
# There is a hard limit of 9216 possibilities, and we do O(1) work for each of them
# Our intermediate arrays are at most 4 elements, and the number made is bounded by an O(1) factor
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 0.001 # cannot judge ==
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    left = [num for k, num in enumerate(nums) if k not in {i, j}]
                    if self.judgePoint24([num1 - num2] + left): return True
                    if num2 and self.judgePoint24([num1 / num2] + left): return True
                    if i < j:
                        if self.judgePoint24([num1 + num2] + left): return True
                        if self.judgePoint24([num1 * num2] + left): return True
        return False
