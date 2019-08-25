# Time and space: O(1)
# There is a hard limit of 9216 possibilities, and we do O(1) work for each of them
# Our intermediate arrays are at most 4 elements, and the number made is bounded by an O(1) factor
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        
        def compute(nums):
            if (len(nums) == 1): return abs(nums[0] - 24) < 0.001 # cannot judge ==
            for i, num1 in enumerate(nums):
                for j, num2 in enumerate(nums):
                    if (i != j):
                        others = []
                        for k, num in enumerate(nums):
                            if (k != i and k != j): others.append(num)
                        if (compute(others + [num1 - num2])): return True
                        if (num2 and compute(others + [num1 / num2])): return True
                        if (i < j):
                            if (compute(others + [num1 + num2])): return True
                            if (compute(others + [num1 * num2])): return True
            return False
        
        return compute(nums)
