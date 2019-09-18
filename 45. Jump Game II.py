# Time: O(n), space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        cur = far = 0
        n = len(nums)
        while (cur <= far and far < n - 1):
            step += 1
            for i in range(cur, far + 1): # loop condition is fixed here, not affected by far inside
                far = max(far, i + nums[i])
            cur = i + 1
        return step if far >= n - 1 else -1

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        at = reach = 0
        step = 0
        while at <= reach < n - 1:
            lastreach = reach
            while (at <= lastreach):
                reach = max(reach, at + nums[at])
                at += 1
            if reach > lastreach: step += 1
        return step if reach >= n - 1 else -1
